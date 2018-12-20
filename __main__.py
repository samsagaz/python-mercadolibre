import os
import pprint
from mercadolibre.pyme import PyMe


def main():
    pyme = PyMe(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    pprint.pprint(pyme.get_myself())


if __name__ == "__main__":
    main()
