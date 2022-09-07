import typer

from nhl.utils.context import include_common_params
from nhl.utils.helpers import fetch_with_ctx, print_response_with_ctx

app = typer.Typer(help="Get information about NHL Entry Draft prospects.")


@app.callback(invoke_without_command=True)
@include_common_params
def prospects(
    ctx: typer.Context,
    id: str = typer.Argument("", help="Returns information for a single prospect."),
):
    res = fetch_with_ctx(ctx, f"draft/prospects/{id}")
    print_response_with_ctx(ctx, res)
