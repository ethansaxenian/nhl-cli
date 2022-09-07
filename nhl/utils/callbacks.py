import typer

from nhl.utils.constants import DEFAULT_SEASON, SeasonType, YEAR_FORMAT


def validate_season(value: SeasonType) -> SeasonType:
    if value == DEFAULT_SEASON:
        return value

    if value[1].year - value[0].year != 1:
        raise typer.BadParameter(
            f"{value[0].strftime(YEAR_FORMAT)}-{value[1].strftime(YEAR_FORMAT)} is not a valid NHL season."
        )

    return value
