from dataclasses import dataclass
from typing import Callable

import typer as typer

from nhl.utils.options import NoColors, PrettyFormat, SortKeys
from merge_args import merge_args


@dataclass
class Commons:
    pretty: bool
    sort_keys: bool
    no_colors: bool


def include_common_params(func: Callable) -> Callable:
    @merge_args(func)
    def wrapper(
        ctx: typer.Context,
        pretty: bool = PrettyFormat,
        sort_keys: bool = SortKeys,
        no_colors: bool = NoColors,
        **kwargs,
    ):
        """Setup for finding city."""
        ctx.obj = Commons(pretty, sort_keys, no_colors)
        return func(ctx=ctx, **kwargs)

    return wrapper
