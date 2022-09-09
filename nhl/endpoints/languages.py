import typer

from nhl.utils.helpers import (
    fetch_with_context,
    print_response_with_context,
)
from nhl.utils.options import include_common_options

app = typer.Typer(help="List all support languages.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_options
def languages(ctx: typer.Context):
    res = fetch_with_context(ctx, "languages")
    print_response_with_context(ctx, res)
