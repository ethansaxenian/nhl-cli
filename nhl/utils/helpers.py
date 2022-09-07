import json
from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Optional

import requests
import typer
from merge_args import merge_args
from requests import Response

from nhl.utils.constants import API_BASE_URL, QueryArgs, SeasonType, YEAR_FORMAT
from nhl.utils.options import NoColors, PrettyFormat, SortKeys


def echo(message: str, disable_rich_output: bool = True):
    if not disable_rich_output:
        try:
            from rich import print as rich_print

            rich_print(message)
        except ModuleNotFoundError:
            print(message)
    else:
        print(message)


def fetch(path: str, query_args: Optional[QueryArgs] = None) -> Response:
    query_str = (
        ("?" + "&".join([f"{k}={v}" for k, v in query_args])) if query_args else ""
    )
    url = f"{API_BASE_URL}{path}{query_str}"
    return requests.get(url)


def print_response(
    response: Response,
    pretty: bool = False,
    sort_keys: bool = False,
    no_colors: bool = False,
):
    response_json = json.dumps(
        response.json(), sort_keys=sort_keys, indent=2 if pretty else None
    )
    echo(response_json, no_colors)


def print_response_with_ctx(response: Response, ctx: typer.Context):
    print_response(
        response,
        pretty=ctx.obj.pretty,
        sort_keys=ctx.obj.sort_keys,
        no_colors=ctx.obj.no_colors,
    )


def season_to_str(season: SeasonType) -> str:
    return season[0].strftime(YEAR_FORMAT) + season[1].strftime(YEAR_FORMAT)


def datetime_to_str(time: Optional[datetime], format_str: str) -> str:
    try:
        return time.strftime(format_str)
    except AttributeError:
        return ""


@dataclass
class Commons:
    pretty: bool
    sort_keys: bool
    no_colors: bool


def include_common_params(func: Callable) -> Callable:
    @merge_args(func)
    def wrapper(
        ctx: typer.Context,
        pretty: bool = PrettyFormat,
        sort_keys: bool = SortKeys,
        no_colors: bool = NoColors,
        **kwargs,
    ):
        """Setup for finding city."""
        ctx.obj = Commons(pretty, sort_keys, no_colors)
        return func(ctx=ctx, **kwargs)

    return wrapper
