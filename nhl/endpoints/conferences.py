import typer

from nhl.utils.globals import NoColors, PrettyFormat, SortKeys
from nhl.utils.helpers import fetch, print_response

ConferenceId = typer.Argument("", help="Returns information for a single conference.")


def get_conferences(
    id: str = ConferenceId,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    res = fetch(["conferences", id])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
