import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch, print_response_with_ctx

app = typer.Typer(help="Get information about NHL franchises.")

FranchiseId = typer.Argument(
    "", help="Returns information for a single team instead of the entire league."
)


@app.callback(invoke_without_command=True)
@include_common_params
def franchises(ctx: typer.Context, id: str = FranchiseId):
    res = fetch(f"franchises/{id}")
    print_response_with_ctx(res, ctx)
