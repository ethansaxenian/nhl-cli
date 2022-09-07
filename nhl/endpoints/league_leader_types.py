import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch, print_response_with_ctx

app = typer.Typer(help="List all possible player league leader types.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def league_leader_types(ctx: typer.Context):
    res = fetch(f"leagueLeaderTypes")
    print_response_with_ctx(res, ctx)