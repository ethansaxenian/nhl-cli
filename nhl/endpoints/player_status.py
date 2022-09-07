import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all the player status options")


@app.callback(invoke_without_command=True)
@include_common_params
def player_status(ctx: typer.Context):
    res = fetch(f"playerStatus")
    print_response_with_ctx(res, ctx)
    