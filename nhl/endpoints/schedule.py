from datetime import datetime
from typing import Optional

import typer

from nhl.utils.constants import DATE_FORMAT, DEFAULT_SEASON, SeasonType
from nhl.utils.enums import ScheduleExpands
from nhl.utils.helpers import (
    datetime_to_str,
    fetch_with_context,
    print_response_with_context,
    season_to_str,
)
from nhl.utils.options import ExpandOption, SeasonOption, include_common_options

app = typer.Typer(
    help="Get information about the schedule. By default, returns results for the current day."
)


@app.callback(invoke_without_command=True)
@include_common_options
def schedule(
    ctx: typer.Context,
    expand: list[ScheduleExpands] = ExpandOption,
    team_id: list[str] = typer.Option([], help="Limit results to a specific team(s)."),
    date: Optional[datetime] = typer.Option(
        None, formats=[DATE_FORMAT], help="Single defined date for the search."
    ),
    start_date: Optional[datetime] = typer.Option(
        None, formats=[DATE_FORMAT], help="Start date for the search."
    ),
    end_date: Optional[datetime] = typer.Option(
        None, formats=[DATE_FORMAT], help="End date for the search."
    ),
    season: SeasonType = SeasonOption,
    game_type: Optional[str] = typer.Option(
        None,
        help="Restricts results to certain game types. See 'nhl configurations game-types' for options.",
        show_default="Includes all game types.",
    ),
):
    query_params = []
    for modifier in expand:
        query_params.append(("expand", modifier))
    for name, option in [
        ("date", datetime_to_str(date, DATE_FORMAT)),
        ("startDate", datetime_to_str(start_date, DATE_FORMAT)),
        ("endDate", datetime_to_str(end_date, DATE_FORMAT)),
        ("season", season_to_str(season) if season != DEFAULT_SEASON else None),
        ("gameType", game_type),
    ]:
        if option:
            query_params.append((name, option))
    if len(team_id) > 0:
        query_params.append(("teamId", ",".join(team_id)))

    res = fetch_with_context(ctx, "schedule", query_params)
    print_response_with_context(ctx, res)
