import typer

from nhl.utils.expands import RoundExpands
from nhl.utils.helpers import fetch, print_response
from nhl.utils.options import (
    ExpandOption,
    NoColors,
    PrettyFormat,
    SeasonOption,
    SortKeys,
)

app = typer.Typer(help="Get information about tournaments")


@app.callback(invoke_without_command=True)
def tournaments(
    expand: list[RoundExpands] = ExpandOption,
    season: str = SeasonOption,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    query_params = []
    for modifier in expand:
        query_params.append(("expand", modifier))
    if season is not None:
        query_params.append(("season", season))

    res = fetch(["tournaments", "playoffs"], query_params)
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
