import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch_with_ctx, print_response_with_ctx

app = typer.Typer(help="List all possible draft prospect categories.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def prospect_categories(ctx: typer.Context):
    res = fetch_with_ctx(ctx, f"prospectCategories")
    print_response_with_ctx(ctx, res)
