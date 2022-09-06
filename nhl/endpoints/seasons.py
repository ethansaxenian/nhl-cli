import typer

from nhl.utils.callbacks import validate_season
from nhl.utils.helpers import fetch, print_response
from nhl.utils.options import NoColors, PrettyFormat, SortKeys

app = typer.Typer(help="Get information about NHL seasons.")


@app.callback(invoke_without_command=True)
def seasons(
    season: str = typer.Argument(
        "",
        help="Specify the season. Format: YYYYYYYY (ex: 20202021)",
        show_default="Shows all seasons.",
        callback=lambda val: validate_season(val, allow_current=True),
    ),
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    res = fetch(f"seasons/{season}")
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
