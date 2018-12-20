import os
import pytest
from mercadolibre.pyme import PyMe


def test_env_vars():
    """ Ensure that environment variables are set """
    assert(os.environ['CLIENT_ID'])
    assert(os.environ['CLIENT_SECRET'])
    assert(os.environ['USER_ID'])


def test_init_pyme(mocker):
    mocked_client = mocker.patch("mercadolibre.pyme.BackendApplicationClient")
    mocked_get_token = mocker.patch.object(PyMe, 'get_token')
    pyme = PyMe(client_id="test", client_secret="test")
    assert pyme
    assert mocked_client.called
    mocked_client.assert_called_with(client_id="test", default_token_placement="query")
    assert mocked_get_token.called


def test_create_test_user():
    """
        Mercadolibre just allow to create test user from real ones (MOCK)
    """
    pass


@pytest.mark.vcr()
def test_get_myself():
    """
        TODO
    """
    pyme = PyMe(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    response = pyme.get_myself()
    assert isinstance(response, dict)
    assert 'nickname' in response


@pytest.mark.vcr()
def test_get_user_info():
    """
        TODO
    """
    pyme = PyMe(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    response = pyme.get_user_info(os.environ.get("USER_ID"))
    assert isinstance(response, dict)
    assert 'nickname' in response


@pytest.mark.vcr()
def test_update_user_info():
    """
        TODO
    """
    pyme = PyMe(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    json_data = {'last_name': 'new_last_name'}
    response = pyme.update_user_info(os.environ.get("USER_ID"), json_data)
    assert isinstance(response, dict)
    assert 'user_id' in response


@pytest.mark.vcr()
def test_get_user_address():
    """
        Test user just return empty address list as default
        need to add address to get full working test
    """

    pyme = PyMe(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    response = pyme.get_user_address(os.environ.get("USER_ID"))
    keys = []
    for d in response:
        for k in d.keys():
            keys.append(k)
    assert isinstance(response, list)


@pytest.mark.vcr()
def test_get_user_info_accepted_payment_methods():
    """
        TODO
    """

    pyme = PyMe(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    response = pyme.get_user_info_accepted_payment_methods(os.environ.get("USER_ID"))
    keys = []
    for d in response:
        for k in d.keys():
            keys.append(k)
    assert 'payment_type_id' in keys
    assert isinstance(response, list)


@pytest.mark.vcr()
def test_get_application_details():
    """
        TODO
    """
    pyme = PyMe(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    response = pyme.get_application_details(os.environ.get("CLIENT_ID"))
    assert isinstance(response, dict)
    assert 'certification_status' in response


@pytest.mark.vcr()
def test_get_user_brands():
    """
        TODO
    """
    pyme = PyMe(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    response = pyme.get_user_brands(58715193)
    assert isinstance(response, dict)
    assert 'cust_id' in response


@pytest.mark.vcr()
def test_get_available_listing_types():
    """
        TODO
    """
    pyme = PyMe(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    response = pyme.get_available_listing_types(os.environ.get("USER_ID"))
    assert isinstance(response, dict)
    assert 'available' in response


@pytest.mark.vcr()
def test_get_user_feeds():
    """
        TODO
    """
    pyme = PyMe(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    response = pyme.get_user_feeds(os.environ.get("CLIENT_ID"))
    assert isinstance(response, dict)
    assert 'messages' in response
