import typer

from nhl.utils.constants import DEFAULT_SEASON, SeasonType
from nhl.utils.enums import TeamExpands
from nhl.utils.helpers import (
    fetch_with_context,
    print_response_with_context,
    season_to_str,
)
from nhl.utils.options import ExpandOption, SeasonOption, include_common_options

app = typer.Typer(help="Get information about NHL teams.")


@app.callback(invoke_without_command=True)
@include_common_options
def teams(
    ctx: typer.Context,
    id: str = typer.Argument(
        "", help="Returns information for a single team instead of the entire league."
    ),
    expand: list[TeamExpands] = ExpandOption,
    season: SeasonType = SeasonOption,
    team_id: list[str] = typer.Option([], help="Can specify multiple team ids."),
    roster: bool = typer.Option(
        False, "--roster", help="Include the entire roster of a team."
    ),
    stats: bool = typer.Option(
        False,
        "--stats",
        help=(
            "Include current season stats and the current season rankings for a specific team. "
            "(Note: Has no effect if --roster option is set.)"
        ),
    ),
):
    if not id and (roster or stats):
        raise typer.BadParameter(
            "--roster and --stats options must also specify a team Id"
        )

    query_params = []
    for modifier in expand:
        query_params.append(("expand", modifier))
    if len(team_id) > 0:
        query_params.append(("teamId", ",".join(team_id)))
    if season != DEFAULT_SEASON:
        query_params.append(("season", season_to_str(season)))

    res = fetch_with_context(
        ctx,
        f"teams/{id}/{'roster' if roster else 'stats' if stats else ''}",
        query_params,
    )
    print_response_with_context(ctx, res)
