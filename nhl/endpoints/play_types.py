import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch, print_response_with_ctx

app = typer.Typer(help="List all play types.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def play_types(ctx: typer.Context):
    res = fetch(f"playTypes")
    print_response_with_ctx(res, ctx)