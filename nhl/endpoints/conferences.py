import typer

from nhl.utils.helpers import fetch, print_response
from nhl.utils.options import NoColors, PrettyFormat, SortKeys

app = typer.Typer(help="Get information about NHL conferences.")

ConferenceId = typer.Argument("", help="Returns information for a single conference.")


@app.callback(invoke_without_command=True)
def conferences(
    id: str = ConferenceId,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    res = fetch(["conferences", id])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
