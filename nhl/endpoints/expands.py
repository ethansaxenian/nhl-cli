import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all expands.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def expands(ctx: typer.Context):
    res = fetch(f"expands")
    print_response_with_ctx(res, ctx)
    