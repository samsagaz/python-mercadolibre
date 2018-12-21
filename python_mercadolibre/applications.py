"""
python-mercadolibre
~~~~~~~~~~~~~~~~~~~
*python-mercadolibre* is a wrapper, written in Python, for MercadoLibre API v2.0
By calling the functions available in *python-mercadolibre* you can simplify
your code and easily access to all the features available in the MercadoLibre API

:copyright: (c) 2018-2019 by Jose Luis Zanotti.

:license: GPLv3, see LICENSE for more details
"""

from .base import PyMe


class Applications(PyMe):

    def get_details(self, application_id):
        """ Get application details """
        endpoint = f"/applications/{application_id}"
        return self._call_api('get', endpoint)
