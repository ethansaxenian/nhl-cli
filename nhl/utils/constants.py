from datetime import datetime

API_BASE_URL = "https://statsapi.web.nhl.com/api/v1/"

QueryArgs = list[tuple[str, str]]

SeasonType = tuple[datetime, datetime]

# use this as 'None' since Optional[tuple[datetime, datetime]] doesn't seem to work for a typer option type.
DEFAULT_SEASON: SeasonType = (datetime(1, 1, 1, 0, 0), datetime(1, 1, 1, 0, 0))

YEAR_FORMAT = "%Y"

DATE_FORMAT = "%Y-%m-%d"
