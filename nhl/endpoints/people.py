from typing import Optional

import typer

from nhl.utils.constants import DEFAULT_SEASON, SeasonType
from nhl.utils.enums import PersonExpands, StatType
from nhl.utils.helpers import (
    fetch_with_context,
    print_response_with_context,
    season_to_str,
)
from nhl.utils.options import ExpandOption, SeasonOption, include_common_options

app = typer.Typer(help="Gets details for a player.")


@app.callback(invoke_without_command=True)
@include_common_options
def people(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="ID for the player.", show_default=False),
    stats: Optional[StatType] = typer.Option(
        None, "--stats", help="Include additional player stats."
    ),
    season: SeasonType = SeasonOption,
    expand: list[PersonExpands] = ExpandOption,
):
    query_args = []
    if stats is not None:
        query_args.append(("stats", stats))
    if season != DEFAULT_SEASON:
        query_args.append(("season", season_to_str(season)))
    for modifier in expand:
        query_args.append(("expand", modifier))

    res = fetch_with_context(
        ctx, f"people/{id}/{'stats' if stats is not None else ''}", query_args
    )
    print_response_with_context(ctx, res)
