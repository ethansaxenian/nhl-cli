import typer

from nhl.utils.callbacks import validate_season
from nhl.utils.constants import DEFAULT_SEASON, YEAR_FORMAT

PrettyFormat = typer.Option(False, "--pretty", "-p", help="Format output.")

SortKeys = typer.Option(False, "--sort-keys", "-s", help="Sort output.")

NoColors = typer.Option(False, "--no-colors", "-n", help="Disable colored output.")

ExpandOption = typer.Option(
    [], "--expand", "-e", help="See 'nhl configurations expands' for details."
)

SeasonOption = typer.Option(
    DEFAULT_SEASON,
    formats=[YEAR_FORMAT],
    help="Specify the season.",
    show_default="Uses the current season.",
    callback=validate_season,
)
