import typer

from nhl.utils.helpers import fetch, include_common_params, print_response_with_ctx

app = typer.Typer(help="List all possible series codes")


@app.callback(invoke_without_command=True)
@include_common_params
def series_codes(ctx: typer.Context):
    res = fetch(f"seriesCodes")
    print_response_with_ctx(res, ctx)
    