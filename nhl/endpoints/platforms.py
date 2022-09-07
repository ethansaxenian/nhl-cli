import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all possible platforms")


@app.callback(invoke_without_command=True)
@include_common_params
def platforms(ctx: typer.Context):
    res = fetch(f"platforms")
    print_response_with_ctx(res, ctx)
    