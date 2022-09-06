from typing import Optional

import typer

from nhl.endpoints.conferences import ConferenceId, get_conferences
from nhl.endpoints.divisions import DivisionId, get_divisions
from nhl.endpoints.franchises import FranchiseId, get_franchises
from nhl.endpoints.teams import (
    RosterOption,
    StatsOption,
    TeamId,
    TeamIdOption,
    get_teams,
)
from nhl.utils.globals import (
    ExpandOption,
    NoColors,
    PrettyFormat,
    SeasonOption,
    SortKeys,
)
from nhl.utils.helpers import fetch, print_response

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
    no_colors: bool = NoColors,
):
    get_teams(id, expand, season, team_id, roster, stats, pretty, sort_keys, no_colors)


@app.command(help="Get information about NHL franchises.")
def franchises(
    id: str = FranchiseId,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    get_franchises(id, pretty, sort_keys, no_colors)


@app.command(help="Get information about NHL divisions.")
def divisions(
    id: str = DivisionId,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    get_divisions(id, pretty, sort_keys, no_colors)


@app.command(help="Get information about NHL conferences.")
def conferences(
    id: str = ConferenceId,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    get_conferences(id, pretty, sort_keys, no_colors)


@app.command(help="List all configuration endpoints")
def configurations(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    print_response(
        fetch(["configurations"]),
        pretty=pretty,
        sort_keys=sort_keys,
        no_colors=no_colors,
    )


@app.command(help="List all supported languages")
def languages(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    print_response(
        fetch(["languages"]), pretty=pretty, sort_keys=sort_keys, no_colors=no_colors
    )


@app.command(help="List all expands")
def expands(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    print_response(
        fetch(["expands"]), pretty=pretty, sort_keys=sort_keys, no_colors=no_colors
    )


def platforms(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    print_response(
        fetch(["platforms"]), pretty=pretty, sort_keys=sort_keys, no_colors=no_colors
    )


if __name__ == "__main__":
    app()
