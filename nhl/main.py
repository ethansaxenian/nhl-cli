from typing import Optional

import typer

from nhl.endpoints.franchises import FranchiseId, get_franchises
from nhl.endpoints.teams import (
    RosterOption,
    StatsOption,
    TeamId,
    TeamIdOption,
    get_teams,
)
from nhl.utils.globals import ExpandOption, PrettyFormat, SeasonOption, SortKeys

app = typer.Typer(
    name="nhl", help="An NHL API CLI", add_completion=False, no_args_is_help=True
)


@app.command(help="Get information about NHL teams.")
def teams(
    id: str = TeamId,
    expand: list[str] = ExpandOption,
    season: Optional[str] = SeasonOption,
    team_id: list[str] = TeamIdOption,
    roster: bool = RosterOption,
    stats: bool = StatsOption,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
):
    get_teams(id, expand, season, team_id, roster, stats, pretty, sort_keys)


@app.command(help="Get information about NHL franchises.")
def franchises(
    id: str = FranchiseId,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
):
    get_franchises(id, pretty, sort_keys)


if __name__ == "__main__":
    app()
