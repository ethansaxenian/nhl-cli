import typer

from nhl.utils.constants import DEFAULT_SEASON, SeasonType
from nhl.utils.expands import StandingsExpands
from nhl.utils.helpers import fetch, print_response, season_to_str
from nhl.utils.options import (
    ExpandOption,
    NoColors,
    PrettyFormat,
    SeasonOption,
    SortKeys,
)

app = typer.Typer(help="Get information about standings.")


@app.callback(invoke_without_command=True)
def standings(
    expand: list[StandingsExpands] = ExpandOption,
    season: SeasonType = SeasonOption,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    query_params = []
    for modifier in expand:
        query_params.append(("expand", modifier))
    if season != DEFAULT_SEASON:
        query_params.append(("season", season_to_str(season)))

    res = fetch("standings", query_params)
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
