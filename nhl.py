from typing import Optional

import typer

from globals import PrettyFormat, SortKeys
from helpers import fetch, print_response

app = typer.Typer(name="nhl", help="An NHL API CLI", add_completion=False)


@app.command()
def teams(
    id: str = typer.Argument(
        "", help="The ID of the team.", show_default="Gets all teams."
    ),
    expand: list[str] = typer.Option([], help="See nhl expands for details."),
    season: Optional[str] = typer.Option(None, help="Specify the season."),
    team_id: list[str] = typer.Option(
        [], "--teamId", help="Can specify multiple team ids."
    ),
    roster: bool = typer.Option(
        False,
        "--roster",
        help="Returns entire roster for a team including id value, name, jersey number and position details.",
    ),
    stats: bool = typer.Option(
        False,
        "--stats",
        help="Returns current season stats and the current season rankings for a specific team.",
    ),
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
):
    """
    Get information about NHL teams.
    """
    query_params = []
    for modifier in expand:
        query_params.append(("expand", modifier))
    if len(team_id) > 0:
        query_params.append(("teamId", ",".join(team_id)))
    if season is not None:
        query_params.append(("season", season))

    res = fetch(
        "teams",
        query_params,
        id,
        "roster" if roster else "stats" if stats else "",
    )
    print_response(res, pretty=pretty, sort_keys=sort_keys)


@app.command()
def franchises(
    id: str = typer.Argument(
        default="", help="The ID of the franchise.", show_default="Gets all franchises."
    ),
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
):
    """
    Get information about NHL franchises.
    """
    res = fetch(f"franchises/{id}")
    print_response(res, pretty=pretty, sort_keys=sort_keys)


if __name__ == "__main__":
    app()
