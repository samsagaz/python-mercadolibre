import os
import pytest
import python_mercadolibre as pyme
from python_mercadolibre.users.models import Profile


def test_create_test_user():
    """
        Mercadolibre just allow to create test user from real accounts (MOCK)
    """
    pass


@pytest.mark.vcr()
def test_user_profile():
    user = pyme.User()
    response = user.profile()
    assert type(response) == Profile


@pytest.mark.vcr()
def test_get_user_info():
    """
        TODO
    """
    user = pyme.User()
    response = user.get_user_info(os.environ.get("USER_ID"))
    assert isinstance(response, dict)
    assert "nickname" in response


@pytest.mark.vcr()
def test_update_user_info():
    """
        TODO
    """
    user = pyme.User()
    json_data = {"last_name": "new_last_name"}
    response = user.update_user_info(os.environ.get("USER_ID"), json_data)
    assert isinstance(response, dict)
    assert "user_id" in response


@pytest.mark.vcr()
def test_get_user_address():
    """
        Test user just return empty address list as default
        need to add address to get full working test
    """

    user = pyme.User()
    response = user.get_user_address(os.environ.get("USER_ID"))
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

    user = pyme.User()
    response = user.get_user_info_accepted_payment_methods(os.environ.get("USER_ID"))
    keys = []
    for d in response:
        for k in d.keys():
            keys.append(k)
    assert "payment_type_id" in keys
    assert isinstance(response, list)


@pytest.mark.vcr()
def test_get_user_brands():
    """
        TODO
    """
    user = pyme.User()
    response = user.get_user_brands(58_715_193)
    assert isinstance(response, dict)
    assert "cust_id" in response


@pytest.mark.vcr()
def test_get_available_listing_types():
    """
        TODO
    """
    user = pyme.User()
    response = user.get_available_listing_types(os.environ.get("USER_ID"))
    assert isinstance(response, dict)
    assert "available" in response


@pytest.mark.vcr()
def test_get_user_feeds():
    """
        TODO
    """
    user = pyme.User()
    response = user.get_user_feeds(os.environ.get("CLIENT_ID"))
    assert isinstance(response, dict)
    assert "messages" in response
