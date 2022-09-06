import json
from typing import Optional

import requests
from requests import Response

API_BASE_URL = "https://statsapi.web.nhl.com/api/v1"

QueryArgs = list[tuple[str, str]]


def fetch(paths: list[str], query_args: Optional[QueryArgs] = None) -> Response:
    path_str = "/".join(paths)
    query_str = "&".join([f"{k}={v}" for k, v in query_args]) if query_args else ""
    url = f"{API_BASE_URL}/{path_str}?{query_str}"
    return requests.get(url)


def print_response(
    response: Response, pretty: bool = False, sort_keys: bool = False
) -> None:
    response_json = json.dumps(
        response.json(), sort_keys=sort_keys, indent=2 if pretty else None
    )
    try:
        from rich import print as rich_print

        rich_print(response_json)
    except ModuleNotFoundError:
        print(response_json)
