import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all status types")


@app.callback(invoke_without_command=True)
@include_common_params
def game_status(ctx: typer.Context):
    res = fetch(f"gameStatus")
    print_response_with_ctx(res, ctx)
    