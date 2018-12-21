import pytest
from python_mercadolibre.users.models import Profile


def test_user_profile_ok():
    kwargs = {'nickname': 'a nick name'}
    profile = Profile(**kwargs)

    assert profile.nickname == 'a nick name'


def test_user_profile_without_name():
    kwargs = {'name': 'a  name'}
    profile = Profile(**kwargs)

    with pytest.raises(AttributeError) as excinfo:
        profile.nickname

    assert "'Profile' object has no attribute 'nickname'" in str(excinfo.value)
