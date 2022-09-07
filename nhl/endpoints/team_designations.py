import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch, print_response_with_ctx

app = typer.Typer(help="List all possible team designations.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def team_designations(ctx: typer.Context):
    res = fetch(f"teamDesignations")
    print_response_with_ctx(res, ctx)
