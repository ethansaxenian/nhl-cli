import typer

from nhl.utils.globals import PrettyFormat, SortKeys
from nhl.utils.helpers import fetch, print_response

FranchiseId = typer.Argument(
    "", help="Returns information for a single team instead of the entire league."
)


def get_franchises(
    id: str = FranchiseId,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
):
    res = fetch(["franchises", id])
    print_response(res, pretty=pretty, sort_keys=sort_keys)
