import typer

from nhl.utils.enums import AwardsExpands
from nhl.utils.helpers import fetch_with_context, print_response_with_context
from nhl.utils.options import ExpandOption, include_common_options

app = typer.Typer(help="Get information about awards.")

AwardId = typer.Argument("", help="Returns information for a single award.")


@app.callback(invoke_without_command=True)
@include_common_options
def awards(
    ctx: typer.Context,
    id: str = AwardId,
    expand: list[AwardsExpands] = ExpandOption,
):
    res = fetch_with_context(
        ctx, f"awards/{id}", [("expand", modifier) for modifier in expand]
    )
    print_response_with_context(ctx, res)
