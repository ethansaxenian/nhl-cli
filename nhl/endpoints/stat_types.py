import typer

from nhl.utils.helpers import fetch, print_response_with_ctx
from nhl.utils.context import include_common_params

app = typer.Typer(help="List all stat types.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def stat_types(ctx: typer.Context):
    res = fetch(f"statTypes")
    print_response_with_ctx(res, ctx)
