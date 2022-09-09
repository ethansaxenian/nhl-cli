import typer

from nhl.utils.helpers import (
    fetch_with_context,
    print_response_with_context,
)
from nhl.utils.options import include_common_options

app = typer.Typer(help="Get information about NHL Entry Draft prospects.")


@app.callback(invoke_without_command=True)
@include_common_options
def prospects(
    ctx: typer.Context,
    id: str = typer.Argument("", help="Returns information for a single prospect."),
):
    res = fetch_with_context(ctx, f"draft/prospects/{id}")
    print_response_with_context(ctx, res)
