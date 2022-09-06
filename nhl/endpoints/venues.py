import typer

from nhl.utils.helpers import fetch, print_response
from nhl.utils.options import NoColors, PrettyFormat, SortKeys

app = typer.Typer(help="Get information about venues.")

VenueId = typer.Argument("", help="Returns information for a single venue.")


@app.callback(invoke_without_command=True)
def venues(
    id: str = VenueId,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    res = fetch(f"venues/{id}")
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
