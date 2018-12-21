"""
Base Class of Python-Mercadolibre
"""
import json
import os
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from .exceptions import APIError


class PyMe:
    def __init__(self):
        self.base_url = "https://api.mercadolibre.com"
        self.client_id = os.environ.get("CLIENT_ID")
        self.client_secret = os.environ.get("CLIENT_SECRET")
        self.client = BackendApplicationClient(
            client_id=self.client_id,
            default_token_placement="query")
        self.session = OAuth2Session(client=self.client)
        self.token = self.get_token()

    def set_token(self):
        if not self.token:
            self.token = self.get_token()
        self.session.params = {"access_token": self.token}

    def get_token(self):
        token = self.session.fetch_token(
            token_url=self.base_url + "/oauth/token", client_id=self.client_id, client_secret=self.client_secret)
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
