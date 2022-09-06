import typer

from nhl.utils.helpers import fetch, print_response
from nhl.utils.options import NoColors, PrettyFormat, SortKeys

app = typer.Typer(help="Get information about NHL Entry Draft prospects.")


@app.callback(invoke_without_command=True)
def prospects(
    id: str = typer.Argument("", help="Returns information for a single prospect."),
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    res = fetch(f"draft/prospects/{id}")
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
