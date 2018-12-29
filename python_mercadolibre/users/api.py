from python_mercadolibre.base import PyMe
from .models import Profile
from python_mercadolibre.questions.models import QuestionModel


class Search(PyMe):
    search_url = "/sites"
    search_by_id_url = "/search?id="
    search_by_nick_url = "/search?nickname="

    def full_url(self, relativ_url, arg, site_id="MLA"):
        return f"{self.search_url}/{site_id}{relativ_url}{arg}"

    def user(self, user_id=None, nickname=None):
        if user_id:
            url = self.full_url(self.search_by_id_url, user_id)
        if nickname:
            url = self.full_url(self.search_by_nick_url, nickname)

        data = self._call_api('get', url)
        if not data:
            return "User not found"

        return data


class User(PyMe):
    """
    Mercadolibre API Users Funcionality
    See: https://api.mercadolibre.com/users

    """
    user_url = "/users"
    profile_url = "/me"

    URLS = {
        'myself': '/users/me',
        'test_user': '/test_user',
        'user_info': '/users/{user_id}',
    }

    def __repr__(self):
        return "<Pyme-Api-User>"

    def full_url(self, relativ_url):
        return f"{self.user_url}{relativ_url}"

    def profile(self):
        """ Get information about registered user."""
        data = self._call_api('get', self.full_url(self.profile_url))
        return Profile(**data)

    def blacklisted_questions(self, user_id):
        """ Get blacklisted questions from user """
        url = self.full_url(f"/{user_id}/questions_blacklist")
        data = self._call_api('get', url)
        if not data:
            return "Question not found"
        return QuestionModel(**data)

    def create_test_user(self, site_id):

        endpoint = f"/users/test_user"
        json_data = {
            'site_id': site_id
            }
        return self._call_api('post', endpoint, json_data=json_data)

    def get_user_info(self, user_id):
        """ Get user information """
        return self._call_api('get', self.URLS['user_info'].format(user_id=user_id))

    def update_user_info(self, user_id, json_data=None):
        """ Update user information """

        endpoint = f"/users/{user_id}"
        return self._call_api('put', endpoint, json_data)

    def get_user_address(self, user_id):
        """ Get user addresses """

        endpoint = f"/users/{user_id}/addresses"
        return self._call_api('get', endpoint)

    def get_user_info_accepted_payment_methods(self, user_id):
        """ Get accepted payment methods by user """

        endpoint = f"/users/{user_id}/accepted_payment_methods"
        return self._call_api('get', endpoint)

    def get_user_feeds(self, app_id):
        """ Get historic of notifications by app """

        endpoint = f"/myfeeds?app_id={app_id}"
        return self._call_api('get', endpoint)

    def get_user_brands(self, user_id):
        """ Get brands by user """

        endpoint = f"/users/{user_id}/brands"
        return self._call_api('get', endpoint)

    def get_user_classifieds_promotion_packs(self, user_id):
        """ Get promotions packs engaged by user """
        endpoint = f"/users/{user_id}/classifieds_promotion_packs"
        return self._call_api('get', endpoint)

    def create_user_classifieds_promotion_packs(self, user_id, json_data):
        """ Creates a new Promotion Pack for the user """

        endpoint = f"/users/{user_id}/classifieds_promotion_packs"
        return self._call_api('post', endpoint, json_data)

    def get_available_listing_type_by_user_and_category(self, user_id, listing_type, category_id):
        """ Get the availability Listing Type availability by user and category """

        endpoint = f"/users/{user_id}/classifieds_promotion_packs/{listing_type}&categoryId={category_id}"
        return self._call_api('get', endpoint)

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
