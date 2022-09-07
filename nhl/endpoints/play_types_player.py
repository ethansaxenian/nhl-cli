import typer

from nhl.utils.helpers import fetch, print_response_with_ctx
from nhl.utils.context import include_common_params

app = typer.Typer(help="List all play types for player.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def play_types_player(ctx: typer.Context):
    res = fetch(f"playTypesPlayer")
    print_response_with_ctx(res, ctx)
