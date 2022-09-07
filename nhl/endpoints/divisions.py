import typer

from nhl.utils.expands import DivisionExpands
from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx
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
    res = fetch(f"divisions/{id}", [("expand", modifier) for modifier in expand])
    print_response_with_ctx(res, ctx)
