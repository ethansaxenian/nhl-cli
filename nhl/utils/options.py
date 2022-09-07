import typer

from nhl.utils.callbacks import validate_season
from nhl.utils.constants import DEFAULT_SEASON, YEAR_FORMAT

ExpandOption = typer.Option([], "--expand", "-e", help="See 'nhl expands' for details.")

SeasonOption = typer.Option(
    DEFAULT_SEASON,
    formats=[YEAR_FORMAT],
    help="Specify the season.",
    show_default="Uses the current season.",
    callback=validate_season,
)
