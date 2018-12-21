import os
import pprint
import python_mercadolibre as pyme


def main():
    applications = pyme.Applications()
    pprint.pprint(applications.get_details(os.environ.get("CLIENT_ID")))


if __name__ == "__main__":
    main()
