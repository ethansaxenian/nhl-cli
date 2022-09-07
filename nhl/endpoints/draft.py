from datetime import datetime
from typing import Optional

import typer

from nhl.utils.constants import YEAR_FORMAT
from nhl.utils.helpers import datetime_to_str, fetch, print_response
from nhl.utils.options import NoColors, PrettyFormat, SortKeys

app = typer.Typer(help="Get round-by-round data for the NHL Entry Draft.")


@app.callback(invoke_without_command=True)
def draft(
    year: Optional[datetime] = typer.Argument(
        None,
        formats=[YEAR_FORMAT],
        help="Specify the draft year.",
        show_default="Shows the current year's draft.",
    ),
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    res = fetch(f"draft/{datetime_to_str(year, YEAR_FORMAT)}")
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
