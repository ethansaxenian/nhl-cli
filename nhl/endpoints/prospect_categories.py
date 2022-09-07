import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all possible draft prospect categories")


@app.callback(invoke_without_command=True)
@include_common_params
def prospect_categories(ctx: typer.Context):
    res = fetch(f"prospectCategories")
    print_response_with_ctx(res, ctx)
    