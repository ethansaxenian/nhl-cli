import json

import requests
from requests import Response

API_BASE_URL = "https://statsapi.web.nhl.com/api/v1/"


def fetch(endpoint: str) -> Response:
    return requests.get(f"{API_BASE_URL}{endpoint}")


def print_response(
    response: Response, pretty: bool = False, sort_keys: bool = False
) -> None:
    print(
        json.dumps(response.json(), sort_keys=sort_keys, indent=2 if pretty else None)
    )
