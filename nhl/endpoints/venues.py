import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch, print_response_with_ctx

app = typer.Typer(help="Get information about venues.")

VenueId = typer.Argument("", help="Returns information for a single venue.")


@app.callback(invoke_without_command=True)
@include_common_params
def venues(ctx: typer.Context, id: str = VenueId):
    res = fetch(f"venues/{id}")
    print_response_with_ctx(res, ctx)
