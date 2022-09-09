import typer

from nhl.utils.helpers import (
    fetch_with_context,
    print_response_with_context,
)
from nhl.utils.options import include_common_options

app = typer.Typer(help="Get information about venues.")

VenueId = typer.Argument("", help="Returns information for a single venue.")


@app.callback(invoke_without_command=True)
@include_common_options
def venues(ctx: typer.Context, id: str = VenueId):
    res = fetch_with_context(ctx, f"venues/{id}")
    print_response_with_context(ctx, res)
