import typer

from nhl.utils.constants import DEFAULT_SEASON, SeasonType
from nhl.utils.expands import RoundExpands
from nhl.utils.helpers import (
    fetch_with_context,
    print_response_with_context,
    season_to_str,
)
from nhl.utils.options import ExpandOption, SeasonOption, include_common_options

app = typer.Typer(help="Get information about tournaments")


@app.callback(invoke_without_command=True)
@include_common_options
def tournaments(
    ctx: typer.Context,
    expand: list[RoundExpands] = ExpandOption,
    season: SeasonType = SeasonOption,
):
    query_params = []
    for modifier in expand:
        query_params.append(("expand", modifier))
    if season != DEFAULT_SEASON:
        query_params.append(("season", season_to_str(season)))

    res = fetch_with_context(ctx, "tournaments/playoffs", query_params)
    print_response_with_context(ctx, res)
