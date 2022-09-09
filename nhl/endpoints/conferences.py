import typer

from nhl.utils.helpers import (
    fetch_with_context,
    print_response_with_context,
)
from nhl.utils.options import include_common_options

app = typer.Typer(help="Get information about NHL conferences.")

ConferenceId = typer.Argument("", help="Returns information for a single conference.")


@app.callback(invoke_without_command=True)
@include_common_options
def conferences(ctx: typer.Context, id: str = ConferenceId):
    res = fetch_with_context(ctx, f"conferences/{id}")
    print_response_with_context(ctx, res)
