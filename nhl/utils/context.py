from dataclasses import dataclass
from typing import Callable

import typer as typer
from merge_args import merge_args

from nhl.utils.locales import Locale


@dataclass
class Commons:
    pretty: bool
    sort_keys: bool
    no_colors: bool
    locale: Locale


def include_common_params(func: Callable) -> Callable:
    @merge_args(func)
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
            help="Set the language of the output. See 'nhl site-languages for details'",
        ),
        **kwargs,
    ):
        """Setup for finding city."""
        ctx.obj = Commons(pretty, sort_keys, no_colors, locale)
        return func(ctx=ctx, **kwargs)

    return wrapper
