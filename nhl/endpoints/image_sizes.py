import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all possible image sizes for the logos.")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def image_sizes(ctx: typer.Context):
    res = fetch(f"imageSizes")
    print_response_with_ctx(res, ctx)
    