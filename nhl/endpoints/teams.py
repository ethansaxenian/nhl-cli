from typing import Optional

import typer

from nhl.utils.globals import ExpandOption, PrettyFormat, SeasonOption, SortKeys
from nhl.utils.helpers import fetch, print_response

TeamId = typer.Argument(
    "", help="Returns information for a single team instead of the entire league."
)

TeamIdOption = typer.Option([], "--teamId", help="Can specify multiple team ids.")

RosterOption = typer.Option(
    False, "--roster", help="Include the entire roster of a team."
)

StatsOption = typer.Option(
    False,
    "--stats",
    help="Include current season stats and the current season rankings for a specific team.",
)


def get_teams(
    id: str = TeamId,
    expand: list[str] = ExpandOption,
    season: Optional[str] = SeasonOption,
    team_id: list[str] = TeamIdOption,
    roster: bool = RosterOption,
    stats: bool = StatsOption,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
):
    query_params = []
    for modifier in expand:
        query_params.append(("expand", modifier))
    if len(team_id) > 0:
        query_params.append(("teamId", ",".join(team_id)))
    if season is not None:
        query_params.append(("season", season))

    res = fetch(
        ["teams", id, "roster" if roster else "stats" if stats else ""], query_params
    )
    print_response(res, pretty=pretty, sort_keys=sort_keys)
