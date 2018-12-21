import os
from python_mercadolibre.base import PyMe


def test_env_vars():
    """ Ensure that environment variables are set """
    assert(os.environ['CLIENT_ID'])
    assert(os.environ['CLIENT_SECRET'])
    assert(os.environ['USER_ID'])


def test_init_pyme(mocker):
    mocked_client = mocker.patch("python_mercadolibre.base.BackendApplicationClient")
    mocked_get_token = mocker.patch.object(PyMe, 'get_token')
    pyme = PyMe()

    assert mocked_client.called
    assert mocked_get_token.called
    assert pyme
