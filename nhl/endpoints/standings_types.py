import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all standings types")


@app.callback(invoke_without_command=True)
@include_common_params
def standings_types(ctx: typer.Context):
    res = fetch(f"standingsTypes")
    print_response_with_ctx(res, ctx)
    