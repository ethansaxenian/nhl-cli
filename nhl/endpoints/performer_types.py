import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all possible performer types")


@app.callback(invoke_without_command=True)
@include_common_params
def performer_types(ctx: typer.Context):
    res = fetch(f"performerTypes")
    print_response_with_ctx(res, ctx)
    