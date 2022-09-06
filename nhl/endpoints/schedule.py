from typing import Optional

import typer

from nhl.utils.callbacks import validate_date
from nhl.utils.expands import ScheduleExpands
from nhl.utils.helpers import fetch, print_response
from nhl.utils.options import (
    ExpandOption,
    NoColors,
    PrettyFormat,
    SeasonOption,
    SortKeys,
)

app = typer.Typer(help="Get information about the schedule.")


@app.callback(invoke_without_command=True)
def schedule(
    expand: list[ScheduleExpands] = ExpandOption,
    team_id: list[str] = typer.Option(
        [], "--teamId", help="Limit results to a specific team(s)."
    ),
    date: Optional[str] = typer.Option(
        None, help="Single defined date for the search.", callback=validate_date
    ),
    start_date: Optional[str] = typer.Option(
        None, "--startDate", help="Start date for the search.", callback=validate_date
    ),
    end_date: Optional[str] = typer.Option(
        None, "--endDate", help="End date for the search.", callback=validate_date
    ),
    season: Optional[str] = SeasonOption,
    game_type: Optional[str] = typer.Option(
        None,
        "--gameType",
        help="Restricts results to certain game types. See 'nhl configurations game-types' for options.",
        show_default="Includes all game types.",
    ),
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    query_params = []
    for modifier in expand:
        query_params.append(("expand", modifier))
    for name, option in [
        ("date", date),
        ("startDate", start_date),
        ("endDate", end_date),
        ("season", season),
        ("gameType", game_type),
    ]:
        if option:
            query_params.append((name, option))
    if len(team_id) > 0:
        query_params.append(("teamId", ",".join(team_id)))

    res = fetch(f"schedule", query_params)
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
