import os
import pprint
import json
from mercadolibre.pyme import PyMe


def main():
    pyme = PyMe(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    # pyme = PyMe(client_id=os.environ.get("TEST_CLIENT_ID"), client_secret=os.environ.get("TEST_CLIENT_SECRET"))
    pprint.pprint(pyme.get_myself())
    # pprint.pprint(pyme.get_user_address(387526028))


if __name__ == "__main__":
    main()
