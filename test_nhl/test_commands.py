from typer.testing import CliRunner

from nhl.main import app
from nhl.utils.enums import Locale, StatType

runner = CliRunner()


def test_languages():
    result = runner.invoke(app, ["languages"])
    assert all(locale in result.stdout for locale in list(Locale))


def test_stat_types():
    result = runner.invoke(app, ["stat-types"])
    assert all(stat in result.stdout for stat in list(StatType))
