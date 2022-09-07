import typer

from nhl.utils.helpers import fetch, print_response_with_ctx
from nhl.utils.context import include_common_params

app = typer.Typer(help="List all possible tournament types.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def tournament_types(ctx: typer.Context):
    res = fetch(f"tournamentTypes")
    print_response_with_ctx(res, ctx)
