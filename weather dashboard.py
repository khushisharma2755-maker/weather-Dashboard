
import json
import os

HISTORY_FILE = "history.json"

# Dummy weather data (offline simulation)
DUMMY_WEATHER = {
    "delhi": {"city": "Delhi", "country": "India", "temperature": 32, "weather": "sunny"},
    "mumbai": {"city": "Mumbai", "country": "India", "temperature": 29, "weather": "cloudy"},
    "london": {"city": "London", "country": "UK", "temperature": 18, "weather": "rainy"},
    "new york": {"city": "New York", "country": "USA", "temperature": 22, "weather": "clear"},
    "paris": {"city": "Paris", "country": "France", "temperature": 20, "weather": "windy"},
}

def fetch_weather(city):
    city = city.lower()
    return DUMMY_WEATHER.get(city, None)

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_history(entry):
    history = load_history()
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def show_last_searches(n=5):
    history = load_history()
    if history:
        print(f"\n=== Last {n} Searches ===")
        for record in history[-n:]:
            print(f"{record['city']} ({record['country']}) - {record['temperature']}°C, {record['weather']}")
    else:
        print("\nNo history found!")

def menu():
    while True:
        print("\n=== Weather Dashboard ===")
        print("1. Search weather by city")
        print("2. Show last 5 searches")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            city = input("Enter city name: ")
            data = fetch_weather(city)
            if data:
                print(f"\nWeather in {data['city']}, {data['country']}: {data['temperature']}°C, {data['weather']}")
                save_history(data)
            else:
                print("City not found in dummy database!")
        elif choice == "2":
            show_last_searches()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
     menu()
