import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch, print_response_with_ctx

app = typer.Typer(help="List all status types.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def game_status(ctx: typer.Context):
    res = fetch(f"gameStatus")
    print_response_with_ctx(res, ctx)