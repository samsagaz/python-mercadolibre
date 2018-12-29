"""
python-mercadolibre
~~~~~~~~~~~~~~~~~~~
*python-mercadolibre* is a wrapper, written in Python, for MercadoLibre API v2.0
By calling the functions available in *python-mercadolibre* you can simplify
your code and easily access to all the features available in the MercadoLibre API

:copyright: (c) 2018-2019 by Jose Luis Zanotti.

:license: GPLv3, see LICENSE for more details
"""

__title__ = 'python-mercadolibre'
__version__ = '0.0.1'
__author__ = 'Jose Luis Zanotti'
__copyright__ = 'Copyright (c) 2018-2019 Jose Luis Zanotti'
__license__ = 'GPLv3'

import os
from .base import PyMe
from .applications import Applications
from .users.api import User, Search
from .questions.api import Question

CLIENT_ID = os.environ.get('CLIENT_ID', None)
CLIENT_SECRET = os.environ.get('CLIENT_SECRET', None)
USER_ID = os.environ.get('USER_ID', None)
API_VERSION = '2'
