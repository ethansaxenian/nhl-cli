import typer

from nhl.utils.expands import AwardsExpands
from nhl.utils.helpers import fetch, print_response
from nhl.utils.options import ExpandOption, NoColors, PrettyFormat, SortKeys

app = typer.Typer(help="Get information about awards.")

AwardId = typer.Argument("", help="Returns information for a single award.")


@app.callback(invoke_without_command=True)
def awards(
    id: str = AwardId,
    expand: list[AwardsExpands] = ExpandOption,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    res = fetch(f"awards/{id}", [("expand", modifier) for modifier in expand])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
