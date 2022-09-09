import typer

from nhl.utils.helpers import (
    fetch_with_context,
    print_response_with_context,
)
from nhl.utils.options import include_common_options

app = typer.Typer(help="Get information about NHL franchises.")

FranchiseId = typer.Argument(
    "", help="Returns information for a single team instead of the entire league."
)


@app.callback(invoke_without_command=True)
@include_common_options
def franchises(ctx: typer.Context, id: str = FranchiseId):
    res = fetch_with_context(ctx, f"franchises/{id}")
    print_response_with_context(ctx, res)
