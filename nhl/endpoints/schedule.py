from datetime import datetime
from typing import Optional

import typer

from nhl.utils.constants import DATE_FORMAT, DEFAULT_SEASON, SeasonType
from nhl.utils.expands import ScheduleExpands
from nhl.utils.helpers import datetime_to_str, fetch, print_response, season_to_str
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
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
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

    res = fetch(f"schedule", query_params)
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
