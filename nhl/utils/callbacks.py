import time
from typing import Optional

import typer


def validate_season(value: str, allow_current: bool = False) -> str:
    if not value or (allow_current and value == "current"):
        return value

    allow_current_str = "'current' or " if allow_current else ""
    bad_param_exception = typer.BadParameter(
        f"Only {allow_current_str}a season of the form YYYYYYYY (ex: 20212022) is allowed."
    )

    try:
        if len(value) != 8 or int(value[4:]) - int(value[:4]) != 1:
            raise bad_param_exception
    except ValueError:
        raise bad_param_exception

    return value


def validate_date(value: Optional[str]) -> Optional[str]:
    if not value:
        return value

    try:
        time.strptime(value, "%Y-%m-%d")
    except ValueError:
        raise typer.BadParameter(f"Date must be formatted YYYY-MM-DD")

    return value
