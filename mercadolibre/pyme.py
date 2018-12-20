import json
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from mercadolibre.exceptions import APIError


class PyMe:
    base_url = "https://api.mercadolibre.com"

    def __init__(self, client_id=None, client_secret=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client = BackendApplicationClient(client_id=self.client_id, default_token_placement="query")
        self.session = OAuth2Session(client=self.client)
        self.token = self.get_token()

    def set_token(self):
        if not self.token:
            self.token = self.get_token()
        self.session.params = {"access_token": self.token}

    def get_token(self):
        token = self.session.fetch_token(
            token_url=self.base_url + "/oauth/token", client_id=self.client_id, client_secret=self.client_secret
        )
        return token

    def _call_api(self, method, endpoint, json_data=None):
        if method == 'get':
            response = self.session.get(f"{self.base_url}{endpoint}").json()
        if method == 'put':
            response = self.session.put(f"{self.base_url}{endpoint}", data=json.dumps(json_data)).json()
        if method == 'post':
            response = self.session.post(f"{self.base_url}{endpoint}", data=json.dumps(json_data)).json()
        if method == 'delete':
            response = self.session.delete(f"{self.base_url}{endpoint}")

        if isinstance(response, dict) and 'error' in response:
            raise APIError(response)

        return response

    def create_test_user(self, site_id):
        """ Create Test User to simulate API """

        endpoint = f"/users/test_user"
        json_data = {
            'site_id': site_id
            }
        return self._call_api('post', endpoint, json_data=json_data)

    def get_myself(self):
        """ Get information about the authenticated in user """

        endpoint = f"/users/me"
        return self._call_api('get', endpoint)

    def get_user_info(self, id):
        """ Get user information """

        endpoint = f"/users/{id}"
        return self._call_api('get', endpoint)

    def update_user_info(self, id, json_data=None):
        """ Update user information """

        endpoint = f"/users/{id}"
        return self._call_api('put', endpoint, json_data)

    def get_user_address(self, id):
        """ Get user addresses """

        endpoint = f"/users/{id}/addresses"
        return self._call_api('get', endpoint)

    def get_user_info_accepted_payment_methods(self, id):
        """ Get accepted payment methods by user """

        endpoint = f"/users/{id}/accepted_payment_methods"
        return self._call_api('get', endpoint)

    def get_application_details(self, application_id):
        """ Get application details """
        endpoint = f"/applications/{application_id}"
        return self._call_api('get', endpoint)

    def get_user_brands(self, id):
        """ Get brands by user """

        endpoint = f"/users/{id}/brands"
        return self._call_api('get', endpoint)

    def get_user_classifieds_promotion_packs(self, id):
        """ Get promotions packs engaged by user """
        endpoint = f"/users/{id}/classifieds_promotion_packs"
        return self._call_api('get', endpoint)

    def create_user_classifieds_promotion_packs(self, user_id, json_data):
        """ Creates a new Promotion Pack for the user """

        endpoint = f"/users/{user_id}/classifieds_promotion_packs"
        return self._call_api('post', endpoint, json_data)

    def get_available_listing_type_by_user_and_category(self, user_id, listing_type, category_id):
        """ Get the availability Listing Type availability by user and category """

        endpoint = f"/users/{user_id}/classifieds_promotion_packs/{listing_type}&categoryId={category_id}"
        return self._call_api('get', endpoint)

    def get_user_projects(self):
        """ Get all applications associated to a project """

        endpoint = f"/projects"
        return self._call_api('get', endpoint)

    def create_project(self, json_data):
        """ Create a new project """

        endpoint = f"/projects"
        return self._call_api('post', endpoint, json_data)

    def update_project(self, json_data):
        """ Update a project """

        endpoint = f"/projects"
        return self._call_api('put', endpoint, json_data)

    def remove_project(self):
        """ Remove a project """

        endpoint = f"/projects"
        return self._call_api('delete', endpoint)

    def create_application_under_project(self, project_id, json_data):
        """ Save an application under your project """

        endpoint = f"/projects/{project_id}/applications"
        return self._call_api('post', endpoint, json_data)

    def remove_application_under_project(self, project_id):
        """ Remove an application from your project """

        endpoint = f"/projects/{project_id}/applications"
        return self._call_api('delete', endpoint)

    def get_available_listing_types(self, customer_id):
        """ Get available listing types """

        endpoint = f"/users/{customer_id}/available_listing_types"
        return self._call_api('get', endpoint)

    def get_available_listing_types_for_category(self, customer_id, listing_type_id, category_id):
        """ Get category availability """

        endpoint = f"/users/{customer_id}/available_listing_type/{listing_type_id}?category_id={category_id}"
        return self._call_api('get', endpoint)

    def revoke_app_permissions(self, user_id, app_id):
        """ Revoke permissions to an application """

        endpoint = f"/users/{user_id}/applications/{app_id}"
        return self._call_api('delete', endpoint)

    def get_user_feeds(self, app_id):
        """ Get historic of notifications by app """

        endpoint = f"/myfeeds?app_id={app_id}"
        return self._call_api('get', endpoint)
