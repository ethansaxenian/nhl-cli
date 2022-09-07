import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all stat types")


@app.callback(invoke_without_command=True)
@include_common_params
def stat_types(ctx: typer.Context):
    res = fetch(f"statTypes")
    print_response_with_ctx(res, ctx)
    