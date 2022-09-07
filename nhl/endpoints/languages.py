import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all support languages")


@app.callback(invoke_without_command=True)
@include_common_params
def languages(ctx: typer.Context):
    res = fetch(f"languages")
    print_response_with_ctx(res, ctx)
    