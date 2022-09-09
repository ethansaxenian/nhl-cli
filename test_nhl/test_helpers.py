from datetime import datetime

import pytest
import requests
import responses
import typer

from nhl.utils.constants import API_BASE_URL, DEFAULT_SEASON, YEAR_FORMAT
from nhl.utils.helpers import (
    datetime_to_str,
    fetch,
    print_response,
    season_to_str,
    validate_season,
)


@responses.activate
def test_fetch_adds_base_url():
    responses.add(responses.GET, f"{API_BASE_URL}/")
    res = fetch("")
    assert res.url.startswith(API_BASE_URL)


@responses.activate
def test_fetch_adds_query_params():
    responses.add(responses.GET, f"{API_BASE_URL}/?param=value")
    res = fetch("", [("param", "value")])
    assert "?param=value" in res.url


@responses.activate
def test_fetch_adds_multiple_query_params():
    responses.add(responses.GET, f"{API_BASE_URL}/?param=value&param2=value2")
    res = fetch("", [("param", "value"), ("param2", "value2")])
    assert "?param=value&param2=value2" in res.url


@responses.activate
def test_print_response(capsys):
    responses.add(responses.GET, API_BASE_URL, json={"a": 1, "b": 2, "c": 3})
    res = requests.get(API_BASE_URL)
    print_response(res)
    out = capsys.readouterr().out
    assert '"a": 1' in out
    assert '"b": 2' in out
    assert '"c": 3' in out


def test_season_to_str():
    season_str = season_to_str((datetime(2021, 1, 1), datetime(2022, 1, 1)))
    assert season_str == "20212022"


def test_datetime_to_str():
    datetime_str = datetime_to_str(datetime(2021, 1, 1), YEAR_FORMAT)
    assert datetime_str == "2021"


def test_datetime_to_str_returns_none_with_no_datetime():
    datetime_str = datetime_to_str(None, "")
    assert datetime_str == ""


def test_validate_season():
    season = (datetime(2021, 1, 1), datetime(2022, 1, 1))
    value = validate_season(season)
    assert value == season


def test_validate_season_with_default_season():
    value = validate_season(DEFAULT_SEASON)
    assert value == DEFAULT_SEASON


def test_validate_season_raises_error_with_difference_of_two_years():
    with pytest.raises(typer.BadParameter):
        season = (datetime(2020, 1, 1), datetime(2022, 1, 1))
        validate_season(season)


def test_validate_season_raises_error_with_same_years():
    with pytest.raises(typer.BadParameter):
        season = (datetime(2022, 1, 1), datetime(2022, 1, 1))
        validate_season(season)


def test_validate_season_raises_error_with_reversed_years():
    with pytest.raises(typer.BadParameter):
        season = (datetime(2022, 1, 1), datetime(2021, 1, 1))
        validate_season(season)