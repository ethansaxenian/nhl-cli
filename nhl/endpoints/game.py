from datetime import datetime
from typing import Optional

import typer

from nhl.utils.helpers import (
    fetch_with_context,
    print_response_with_context,
)
from nhl.utils.options import include_common_options

app = typer.Typer(help="Get data about an NHL game.")

GameId = typer.Argument(
    ...,
    help=(
        "ID for the game. The first 4 digits identify the season of the game (ie. 2017 for the "
        "2017-2018 season). The next 2 digits give the type of game, where 01 = preseason, "
        "02 = regular season, 03 = playoffs, 04 = all-star. The final 4 digits identify the specific "
        "game number. For regular season and preseason games, this ranges from 0001 to the number of "
        "games played. (1271 for seasons with 31 teams (2017 and onwards) and 1230 for seasons with 30 "
        "teams). For playoff games, the 2nd digit of the specific number gives the round of the "
        "playoffs, the 3rd digit specifies the matchup, and the 4th digit specifies the game (out of "
        "7)."
    ),
    show_default=False,
)


@app.command(name="feed", help="Get all available data for an NHL game.")
@include_common_options
def feed(
    ctx: typer.Context,
    id: str = GameId,
    start_timecode: Optional[datetime] = typer.Option(
        None,
        formats=["%Y%m%d_%H%M%S"],
        help=(
            "Get data after a specific time. You can use this to return a small subset of data relating to game."
        ),
    ),
):
    query_args = [("startTimecode", start_timecode)] if start_timecode else None
    res = fetch_with_context(
        ctx,
        f"game/{id}/feed/live/{'diffPatch' if start_timecode is not None else ''}",
        query_args,
    )
    print_response_with_context(ctx, res)


@app.command(name="boxscore", help="Get the boxscore for an NHL game.")
@include_common_options
def boxscore(ctx: typer.Context, id: str = GameId):
    res = fetch_with_context(ctx, f"game/{id}/boxscore")
    print_response_with_context(ctx, res)


@app.command(name="linescore", help="Get the linescore for an NHL game.")
@include_common_options
def linescore(ctx: typer.Context, id: str = GameId):
    res = fetch_with_context(ctx, f"game/{id}/linescore")
    print_response_with_context(ctx, res)


@app.command(
    name="content",
    help="Get editorials, video replays and photo highlights for an NHL game.",
)
@include_common_options
def content(
    ctx: typer.Context,
    id: str = GameId,
):
    res = fetch_with_context(ctx, f"game/{id}/content")
    print_response_with_context(ctx, res)
