import typer

from nhl.utils.helpers import (
    fetch_with_context,
    print_response_with_context,
)
from nhl.utils.options import include_common_options

app = typer.Typer(help="List all possible positions.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_options
def positions(ctx: typer.Context):
    res = fetch_with_context(ctx, "positions")
    print_response_with_context(ctx, res)
