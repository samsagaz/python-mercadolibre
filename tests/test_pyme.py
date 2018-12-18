import requests_mock
import json
import os
import pprint
import vcr
import copy
from decorators import ignore_warnings
from mercadolibre.pyme import PyMe

# replace sensitive data
def hide_from_response(changes):
    def before_record_response(response):
        strings = response['body']['string'].decode('utf-8')
        body = json.loads(strings)
        for key, value in changes:
            if key in body:
                body[key] = value
        response['body']['string'] = json.dumps(body).encode()
        return response
    return before_record_response

def hide_from_request():
    def before_record_request(request):
        request = copy.deepcopy(request)
        request.uri="https://api.mercadolibre.com/users/me?access_token=APP_USR-HIDDEN-ACCESS-TOKEN"
        return request
    return before_record_request


custom_vcr = vcr.VCR(
    filter_headers=[('Authorization', 'Basic HIDDEN-AUTH-TOKEN')],
    filter_query_parameters=[
        # ('access_token','1234567890'),
        # ('user_id','1234567890'),
        ],
    filter_post_data_parameters=[
        ('client_id','1234567890'),
        ('client_secret','abcdefghi')
        ],
    before_record_response=hide_from_response([
        ('access_token', 'APP_USR-HIDDEN-ACCESS-TOKEN'),
        ('id', 1234567890),
        ('user_id', 123456789),
        ('refresh_token', 'TG-HIDDEN-REFRESH-KEY'),
        ('nickname', 'HIDDEN-NICKNAME'),
        ('last_name', 'HIDDEN-LASTNAME'),
        ('email', 'HIDDEN-EMAIL@gmail.com'),
        ('number', 11111111),
        ('address', 'HIDDEN-ADDRESS'),
        ('permalink', 'http://perfil.mercadolibre.com.ar/')
        ]),
    before_record_request=hide_from_request()
    )


def test_env_vars():
    """ Ensure that environment variables are set """
    assert(os.environ['CLIENT_ID'])
    assert(os.environ['CLIENT_SECRET'])


def test_init_pyme(mocker):
    mocked_client = mocker.patch("mercadolibre.pyme.BackendApplicationClient")
    mocked_get_token = mocker.patch.object(PyMe, 'get_token')
    pyme = PyMe(client_id="test", client_secret="test")
    assert pyme
    assert mocked_client.called
    mocked_client.assert_called_with(client_id="test", default_token_placement="query")
    assert mocked_get_token.called


@vcr.use_cassette('datasets/vcr_cassettes/create_test_user.yaml')
def test_create_test_user():
    """
        Mercadolibre just allow to create test user from real ones (MOCK)
    """
    pass


@ignore_warnings
@custom_vcr.use_cassette('tests/vcr_cassettes/get_myself.yaml')
def test_get_myself():
    """
        TODO
    """
    pyme = PyMe(client_id=os.environ.get("TEST_CLIENT_ID"), client_secret=os.environ.get("TEST_CLIENT_SECRET"))
    response = pyme.get_myself()
    assert 'id' in response


@ignore_warnings
@custom_vcr.use_cassette('tests/vcr_cassettes/get_user_info.yaml')
def test_get_user_info():
    """
        TODO
    """
    pyme = PyMe(client_id=os.environ.get("TEST_CLIENT_ID"), client_secret=os.environ.get("TEST_CLIENT_SECRET"))
    response = pyme.get_user_info(387526028)
    assert 'id' in response


@ignore_warnings
@custom_vcr.use_cassette('tests/vcr_cassettes/update_user_info.yaml')
def test_update_user_info():
    """
        TODO
    """
    pyme = PyMe(client_id=os.environ.get("TEST_CLIENT_ID"), client_secret=os.environ.get("TEST_CLIENT_SECRET"))
    json_data = {'last_name':'new_last_name'}
    response = pyme.update_user_info(387526028, json_data)
    assert isinstance(response, dict)
    assert 'user_id' in response


@ignore_warnings
@custom_vcr.use_cassette('tests/vcr_cassettes/get_user_address.yaml')
def test_get_user_address():
    """
        Test user just return empty address list as default
        need to add address to get full working test
    """

    pyme = PyMe(client_id=os.environ.get("TEST_CLIENT_ID"), client_secret=os.environ.get("TEST_CLIENT_SECRET"))
    response = pyme.get_user_address(387526028)
    assert isinstance(response, list)


@ignore_warnings
@custom_vcr.use_cassette('tests/vcr_cassettes/get_user_info_accepted_payment_methods.yaml')
def test_get_user_info_accepted_payment_methods():
    """

    """

    pyme = PyMe(client_id=os.environ.get("TEST_CLIENT_ID"), client_secret=os.environ.get("TEST_CLIENT_SECRET"))
    response = pyme.get_user_info_accepted_payment_methods(387526028)
    assert isinstance(response, list)
    assert 'id' in response[0]

