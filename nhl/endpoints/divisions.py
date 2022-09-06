import typer

from nhl.utils.expands import DivisionExpands
from nhl.utils.helpers import fetch, print_response
from nhl.utils.options import ExpandOption, NoColors, PrettyFormat, SortKeys

app = typer.Typer(help="Get information about NHL divisions.")

DivisionId = typer.Argument("", help="Returns information for a single division.")


@app.callback(invoke_without_command=True)
def divisions(
    id: str = DivisionId,
    expand: list[DivisionExpands] = ExpandOption,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    res = fetch(["divisions", id], [("expand", modifier) for modifier in expand])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
