import typer

from nhl.utils.expands import DivisionExpands
from nhl.utils.helpers import (
    fetch_with_context,
    print_response_with_context,
)
from nhl.utils.options import ExpandOption, include_common_options

app = typer.Typer(help="Get information about NHL divisions.")

DivisionId = typer.Argument("", help="Returns information for a single division.")


@app.callback(invoke_without_command=True)
@include_common_options
def divisions(
    ctx: typer.Context,
    id: str = DivisionId,
    expand: list[DivisionExpands] = ExpandOption,
):
    res = fetch_with_context(
        ctx, f"divisions/{id}", [("expand", modifier) for modifier in expand]
    )
    print_response_with_context(ctx, res)
