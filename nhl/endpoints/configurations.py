import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch, print_response_with_ctx

app = typer.Typer(help="List all configuration endpoints.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def configurations(ctx: typer.Context):
    res = fetch(f"configurations")
    print_response_with_ctx(res, ctx)
