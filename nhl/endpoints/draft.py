from datetime import datetime
from typing import Optional

import typer

from nhl.utils.constants import YEAR_FORMAT
from nhl.utils.helpers import (
    datetime_to_str,
    fetch_with_context,
    print_response_with_context,
)
from nhl.utils.options import include_common_options

app = typer.Typer(help="Get round-by-round data for the NHL Entry Draft.")


@app.callback(invoke_without_command=True)
@include_common_options
def draft(
    ctx: typer.Context,
    year: Optional[datetime] = typer.Argument(
        None,
        formats=[YEAR_FORMAT],
        help="Specify the draft year.",
        show_default="Shows the current year's draft.",
    ),
):
    res = fetch_with_context(ctx, f"draft/{datetime_to_str(year, YEAR_FORMAT)}")
    print_response_with_context(ctx, res)
