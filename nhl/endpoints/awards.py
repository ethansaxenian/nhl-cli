import typer

from nhl.utils.context import include_common_params
from nhl.utils.expands import AwardsExpands
from nhl.utils.helpers import fetch, print_response_with_ctx
from nhl.utils.options import ExpandOption

app = typer.Typer(help="Get information about awards.")

AwardId = typer.Argument("", help="Returns information for a single award.")


@app.callback(invoke_without_command=True)
@include_common_params
def awards(
    ctx: typer.Context,
    id: str = AwardId,
    expand: list[AwardsExpands] = ExpandOption,
):
    res = fetch(f"awards/{id}", [("expand", modifier) for modifier in expand])
    print_response_with_ctx(res, ctx)
