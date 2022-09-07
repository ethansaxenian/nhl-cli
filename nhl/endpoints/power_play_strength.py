import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all possible platforms")


@app.callback(invoke_without_command=True)
@include_common_params
def power_play_strength(ctx: typer.Context):
    res = fetch(f"powerPlayStrength")
    print_response_with_ctx(res, ctx)
    