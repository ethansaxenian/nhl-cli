import json

import requests
from requests import Response

API_BASE_URL = "https://statsapi.web.nhl.com/api/v1"

QueryArgs = list[tuple[str, str]]


def fetch(endpoint: str, query_args: QueryArgs = None, *paths) -> Response:
    path_str = "/".join(paths)
    query_str = "&".join([f"{k}={v}" for k, v in query_args])
    url = f"{API_BASE_URL}/{endpoint}/{path_str}?{query_str}"
    print(url)
    return requests.get(url)


def print_response(
    response: Response, pretty: bool = False, sort_keys: bool = False
) -> None:
    print(
        json.dumps(response.json(), sort_keys=sort_keys, indent=2 if pretty else None)
    )
