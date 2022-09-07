import typer

from nhl.utils.helpers import fetch, print_response_with_ctx
from nhl.utils.context import include_common_params

app = typer.Typer(help="List all possible schedule types.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def schedule_types(ctx: typer.Context):
    res = fetch(f"scheduleTypes")
    print_response_with_ctx(res, ctx)
