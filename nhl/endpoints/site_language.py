import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="Lists all possible {language}_{site} params..")


@app.callback(invoke_without_command=True, rich_help_panel="Configurations Commands")
@include_common_params
def site_language(ctx: typer.Context):
    res = fetch(f"siteLanguage")
    print_response_with_ctx(res, ctx)
    