import typer


def validate_season(value: str, allow_current: bool = False) -> str:
    if not value or (allow_current and value == "current"):
        return value

    if len(value) != 8 or int(value[4:]) - int(value[:4]) != 1:
        allow_current_str = "'current' or " if allow_current else ""
        raise typer.BadParameter(
            f"Only {allow_current_str}a season of the form YYYYYYYY (ex: 20212022) is allowed."
        )

    return value
