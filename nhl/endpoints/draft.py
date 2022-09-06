import typer

from nhl.utils.helpers import fetch, print_response
from nhl.utils.options import NoColors, PrettyFormat, SortKeys

app = typer.Typer(help="Get round-by-round data for the NHL Entry Draft.")


@app.callback(invoke_without_command=True)
def draft(
    year: str = typer.Argument(
        "",
        help="Specify the draft year. Format: YYYY (ex: 2022)",
        show_default="Shows the current year's draft.",
    ),
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    res = fetch(f"draft/{year}")
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
