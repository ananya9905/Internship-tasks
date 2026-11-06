
import sqlite3
import pytest
import requests

from weather_cli import (
    create_database,
    get_coordinates,
    fetch_weather,
    save_weather
)

class FakeResponse:

    def __init__(self, data, status_code=200):
        self.data = data
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(
                f"HTTP Error: {self.status_code}"
            )

    def json(self):
        return self.data

def test_create_database(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    create_database()

    connection = sqlite3.connect("weather.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name='weather_cache'
    """)

    result = cursor.fetchone()

    connection.close()

    assert result is not None


def test_save_weather(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    create_database()

    save_weather(
        "Nashik",
        19.9975,
        73.7898,
        30.0,
        65,
        12.5,
        "2026-11-06T10:00:00+05:30"
    )

    connection = sqlite3.connect("weather.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT city, temperature, humidity, wind_speed
        FROM weather_cache
    """)

    result = cursor.fetchone()

    connection.close()

    assert result == ("Nashik", 30.0, 65, 12.5)

def test_get_coordinates_success(monkeypatch):

    fake_data = {
        "results": [
            {
                "latitude": 19.9975,
                "longitude": 73.7898
            }
        ]
    }

    def mock_get(*args, **kwargs):
        return FakeResponse(fake_data)

    monkeypatch.setattr(requests, "get", mock_get)

    result = get_coordinates("Nashik")

    assert result == (19.9975, 73.7898)


def test_get_coordinates_city_not_found(monkeypatch):

    fake_data = {
        "results": []
    }

    def mock_get(*args, **kwargs):
        return FakeResponse(fake_data)

    monkeypatch.setattr(requests, "get", mock_get)

    result = get_coordinates("UnknownCity")

    assert result is None


def test_get_coordinates_connection_error(monkeypatch):

    def mock_get(*args, **kwargs):
        raise requests.exceptions.ConnectionError()

    monkeypatch.setattr(requests, "get", mock_get)

    result = get_coordinates("Nashik")

    assert result is None

def test_fetch_weather_success(monkeypatch):

    fake_data = {
        "current": {
            "temperature_2m": 30.0,
            "relative_humidity_2m": 65,
            "wind_speed_10m": 12.5
        }
    }

    def mock_get(*args, **kwargs):
        return FakeResponse(fake_data)

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_weather(19.9975, 73.7898)

    assert result is not None
    assert result[0] == 30.0
    assert result[1] == 65
    assert result[2] == 12.5
    assert isinstance(result[3], str)


def test_fetch_weather_timeout(monkeypatch):

    def mock_get(*args, **kwargs):
        raise requests.exceptions.Timeout()

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_weather(19.9975, 73.7898)

    assert result is None


def test_fetch_weather_invalid_response(monkeypatch):

    fake_data = {
        "unexpected": "invalid response"
    }

    def mock_get(*args, **kwargs):
        return FakeResponse(fake_data)

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_weather(19.9975, 73.7898)

    assert result is None
