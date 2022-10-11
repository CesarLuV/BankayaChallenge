'''This file contains functions for consume external APIs.'''

import requests
from requests.exceptions import HTTPError
from typing import Dict, Optional

from .constants import BASE_EXTERNAL_API_URL as api_url


def consume_api(path: str = None, uri: str = None) -> Dict:
    failure_dict = dict()
    try:
        if not path and not uri:
            raise ValueError("You must provide a valid URI or PATH")

        if path and uri:
            raise ValueError("You must provide only one valid URI or a PATH")

        if path:
            response = requests.get(url=api_url.format(path=path))
        else:
            response = requests.get(url=uri)

        response.raise_for_status()

        return response.json()

    except HTTPError as http_err:
        failure_dict['error'] = f"HTTP error occurred: {http_err}"
    except ValueError as ve:
        failure_dict['error'] = f"Value error: {ve}"
    except Exception as e:
        failure_dict['error'] = f"Exception not considered: {e}"
    return failure_dict