import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all possible positions.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def positions(ctx: typer.Context):
    res = fetch(f"positions")
    print_response_with_ctx(res, ctx)
    