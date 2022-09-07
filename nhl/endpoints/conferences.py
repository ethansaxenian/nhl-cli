import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch_with_ctx, print_response_with_ctx

app = typer.Typer(help="Get information about NHL conferences.")

ConferenceId = typer.Argument("", help="Returns information for a single conference.")


@app.callback(invoke_without_command=True)
@include_common_params
def conferences(ctx: typer.Context, id: str = ConferenceId):
    res = fetch_with_ctx(ctx, f"conferences/{id}")
    print_response_with_ctx(ctx, res)
