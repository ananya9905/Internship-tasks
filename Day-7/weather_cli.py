import sqlite3
import requests
from datetime import datetime

def create_database() -> None:
    with sqlite3.connect("weather.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS weather_cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            city TEXT NOT NULL, 
            latitude REAL NOT NULL, 
            longitude REAL NOT NULL, 
            temperature REAL, 
            humidity INTEGER,   
            wind_speed REAL,
            fetched_at TEXT NOT NULL
        )
        """)

        connection.commit()
    
def get_coordinates(city: str) -> tuple[float, float] | None:
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 5, "language": "en", "format": "json"}
    try:
        geocoding = requests.get(url, params=params, timeout=10)
        geocoding.raise_for_status()
        data = geocoding.json()
        if "results" in data:
            results = data["results"]
            if results:
                latitude = data["results"][0]["latitude"]
                longitude = data["results"][0]["longitude"]
                return (latitude, longitude)
            else:
                print("No city present...")
        else:
            print("No data found...")
    except requests.exceptions.HTTPError as error:
        print("HTTP error:", error)
    except requests.exceptions.ConnectionError as error:
        print("Connection Error:", error)
    except requests.exceptions.Timeout as error:
        print("Connection Time Out...")
    except requests.exceptions.RequestException:
        print("Something went wrong")

def fetch_weather(latitude: float, longitude: float) -> tuple[float, int, float, str] | None:
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {"latitude": latitude, "longitude": longitude, "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "wind_speed_10m", "weather_code"], "timezone": "auto"}
    try:
        weather = requests.get(weather_url, params=weather_params, timeout=10)
        weather.raise_for_status()
        weather_info = weather.json()
        fetched_at = datetime.now().astimezone().isoformat()
        temperature = weather_info["current"]["temperature_2m"]
        humidity = weather_info["current"]["relative_humidity_2m"]
        wind_speed = weather_info["current"]["wind_speed_10m"]
        return (temperature, humidity, wind_speed, fetched_at)
    except requests.exceptions.HTTPError as error:
        print("HTTP error:", error)
    except requests.exceptions.ConnectionError as error:
        print("Connection Error:", error)
    except requests.exceptions.Timeout as error:
        print("Connection Time Out...")
    except ValueError as error:
        print("Invalid Value...")
    except TypeError:
        print("Invalid type")
    except KeyError:
        print("Invalid Key")
    except requests.exceptions.RequestException:
        print("Something went wrong")

def save_weather(city: str, latitude: float, longitude: float, temperature: float, humidity: int, wind_speed: float, fetched_at: str) -> None:
    with sqlite3.connect("weather.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO weather_cache
                        (city, latitude, longitude, temperature, humidity, wind_speed, fetched_at)
                       VALUES(?, ?, ?, ?, ?, ?, ?)""", 
                        (city, latitude, longitude, temperature, humidity, wind_speed, fetched_at))
        connection.commit()

def main() -> None:
    create_database()
    while True:
        city = input("Enter name of the city: ")
        coordinates = get_coordinates(city)
        if not coordinates:
            print("City not found")
            break
        else:
            latitude = coordinates[0]
            longitude = coordinates[1]
        data = fetch_weather(latitude, longitude)
        if not data:
            print("No weather information found")
            break
        else:
            temperature = data[0]
            humidity = data[1]
            wind_speed = data[2]
            fetched_at = data[3]
        save_weather(city, latitude, longitude, temperature, humidity, wind_speed, fetched_at)
        print(f"Temperature of {city.capitalize()}: {temperature} \nHumidity of {city.capitalize()}: {humidity} \nWind speed in {city.capitalize()}: {wind_speed}")
        user = input("Do you want to exit (y/n): ")
        if user == "Y" or user == "y":
            break
        elif user == "N" or user == "n":
            continue
        else:
            print("Please enter valid input")
    
if __name__ == "__main__":
    main()
