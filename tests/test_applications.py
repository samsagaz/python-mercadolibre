import os
import pytest
import python_mercadolibre as pyme


@pytest.mark.vcr()
def test_get_application_details():
    """
        TODO
    """
    applications = pyme.Applications()
    response = applications.get_details(os.environ.get("CLIENT_ID"))
    assert isinstance(response, dict)
    assert 'certification_status' in response
