import json
from datetime import datetime
from typing import Optional

import requests
import typer
from requests import Response

from nhl.utils.constants import API_BASE_URL, QueryArgs, SeasonType, YEAR_FORMAT


def _print(message: str, disable_rich_output: bool = True):
    """
    Prints a message to the console. By default, rich output is enabled but can be disabled.
    If rich is not installed, behaves identically to the built-in print function.
    """
    if not disable_rich_output:
        try:
            from rich import print as rich_print

            rich_print(message)
        except ModuleNotFoundError:
            print(message)
    else:
        print(message)


def fetch(endpoint: str, query_args: Optional[QueryArgs] = None) -> Response:
    """Performs a GET request to the NHL API with a specified endpoint and query arguments."""
    query_str = (
        ("?" + "&".join([f"{k}={v}" for k, v in query_args])) if query_args else ""
    )
    url = f"{API_BASE_URL}{endpoint}{query_str}"
    return requests.get(url)


def fetch_with_context(
    ctx: typer.Context, endpoint: str, query_args: Optional[QueryArgs] = None
):
    """Modifies the API request based on the values from the common cli options."""
    query_args = (query_args or []) + [("locale", ctx.obj.locale)]
    return fetch(endpoint, query_args)


def print_response(
    response: Response,
    pretty: bool = False,
    sort_keys: bool = False,
    no_colors: bool = False,
):
    """Prints an API response to the console."""
    response_json = json.dumps(
        response.json(), sort_keys=sort_keys, indent=2 if pretty else None
    )
    _print(response_json, no_colors)


def print_response_with_context(ctx: typer.Context, response: Response):
    """Modifies the print output based on the values from the common cli options."""
    print_response(
        response,
        pretty=ctx.obj.pretty,
        sort_keys=ctx.obj.sort_keys,
        no_colors=ctx.obj.no_colors,
    )


def season_to_str(season: SeasonType) -> str:
    """Formats a season as a string compatible with the NHL API."""
    return season[0].strftime(YEAR_FORMAT) + season[1].strftime(YEAR_FORMAT)


def datetime_to_str(time: Optional[datetime], format_str: str) -> str:
    """Formats a datetime as a readable string. Returns an empty string if the datetime is None."""
    try:
        return time.strftime(format_str)
    except AttributeError:
        return ""
