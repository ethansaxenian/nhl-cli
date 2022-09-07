import typer

from nhl.utils.callbacks import validate_season
from nhl.utils.constants import DEFAULT_SEASON, SeasonType, YEAR_FORMAT
from nhl.utils.helpers import (
    fetch,
    include_common_params,
    print_response_with_ctx,
    season_to_str,
)

app = typer.Typer(help="Get information about NHL seasons.")


@app.callback(invoke_without_command=True)
@include_common_params
def seasons(
    ctx: typer.Context,
    year: SeasonType = typer.Argument(
        DEFAULT_SEASON,
        formats=[YEAR_FORMAT],
        help="Specify the season. (ex: 2021 2022)",
        show_default="Shows all seasons.",
        callback=validate_season,
    ),
    current: bool = typer.Option(False, "--current", help="Show the current season."),
):
    if current:
        season_str = "current"
    elif year == DEFAULT_SEASON:
        season_str = ""
    else:
        season_str = season_to_str(year)

    res = fetch(f"seasons/{season_str}")
    print_response_with_ctx(res, ctx)
