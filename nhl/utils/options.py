from dataclasses import dataclass
from typing import Callable

import typer
from merge_args import merge_args

from nhl.utils.constants import DEFAULT_SEASON, YEAR_FORMAT
from nhl.utils.enums import Locale
from nhl.utils.helpers import validate_season

ExpandOption = typer.Option(
    [],
    "--expand",
    "-e",
    help="Include additional information. See 'nhl expands' for details.",
)

SeasonOption = typer.Option(
    DEFAULT_SEASON,
    formats=[YEAR_FORMAT],
    help="Specify the season.",
    show_default="Uses the current season.",
    callback=validate_season,
)


@dataclass(frozen=True)
class CommonOptions:
    pretty: bool
    sort_keys: bool
    no_colors: bool
    locale: Locale


def include_common_options(command: Callable) -> Callable:
    """
    A decorator that passes the global cli options to the wrapped command

    See https://github.com/tiangolo/typer/issues/296#issuecomment-869005608
    """

    @merge_args(command)
    def wrapper(
        ctx: typer.Context,
        pretty: bool = typer.Option(False, "--pretty", "-p", help="Format output."),
        sort_keys: bool = typer.Option(False, "--sort-keys", "-s", help="Sort output."),
        no_colors: bool = typer.Option(
            False, "--no-colors", "-n", help="Disable colored output."
        ),
        locale: Locale = typer.Option(
            "en_US",
            "--locale",
            "-l",
            help="Set the language of the output. See 'nhl site-languages' for details.",
        ),
        **kwargs,
    ) -> Callable:
        ctx.obj = CommonOptions(pretty, sort_keys, no_colors, locale)
        return command(ctx=ctx, **kwargs)

    return wrapper
