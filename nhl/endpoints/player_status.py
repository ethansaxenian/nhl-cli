import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch, print_response_with_ctx

app = typer.Typer(help="List all the player status options.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def player_status(ctx: typer.Context):
    res = fetch(f"playerStatus")
    print_response_with_ctx(res, ctx)
