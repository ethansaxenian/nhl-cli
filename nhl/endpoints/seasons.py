import typer

from nhl.utils.callbacks import validate_season
from nhl.utils.constants import DEFAULT_SEASON, SeasonType, YEAR_FORMAT
from nhl.utils.helpers import fetch, print_response, season_to_str
from nhl.utils.options import NoColors, PrettyFormat, SortKeys

app = typer.Typer(help="Get information about NHL seasons.")


@app.callback(invoke_without_command=True)
def seasons(
    year: SeasonType = typer.Argument(
        DEFAULT_SEASON,
        formats=[YEAR_FORMAT],
        help="Specify the season. (ex: 2021 2022)",
        show_default="Shows all seasons.",
        callback=validate_season,
    ),
    current: bool = typer.Option(False, "--current", help="Show the current season."),
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    if current:
        season_str = "current"
    elif year == DEFAULT_SEASON:
        season_str = ""
    else:
        season_str = season_to_str(year)

    res = fetch(f"seasons/{season_str}")
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
