import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch, print_response_with_ctx

app = typer.Typer(help="List all support languages.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def languages(ctx: typer.Context):
    res = fetch(f"languages")
    print_response_with_ctx(res, ctx)
