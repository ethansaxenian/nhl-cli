import typer

from nhl.utils.context import include_common_params
from nhl.utils.expands import DivisionExpands
from nhl.utils.helpers import fetch_with_ctx, print_response_with_ctx
from nhl.utils.options import ExpandOption

app = typer.Typer(help="Get information about NHL divisions.")

DivisionId = typer.Argument("", help="Returns information for a single division.")


@app.callback(invoke_without_command=True)
@include_common_params
def divisions(
    ctx: typer.Context,
    id: str = DivisionId,
    expand: list[DivisionExpands] = ExpandOption,
):
    res = fetch_with_ctx(
        ctx, f"divisions/{id}", [("expand", modifier) for modifier in expand]
    )
    print_response_with_ctx(ctx, res)
