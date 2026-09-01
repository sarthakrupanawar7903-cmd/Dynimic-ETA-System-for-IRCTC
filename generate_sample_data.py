# generate_sample_data.py
# Generates sample live train data for testing

import csv
import random
from app import TRAINS, STATION_NAMES


def generate_sample_data():
    rows = []

    for train in TRAINS:
        train_number = train["number"]
        train_name = train.get("name", f"Train {train_number}")
        route = train["route"]

        station_index = train["current_station_index"]

        # Keep station index within the route
        station_index = max(0, min(station_index, len(route) - 1))

        current_station = route[station_index]

        delay = random.randint(0, 30)
        weather_options = [
            "Clear",
            "Cloudy",
            "Rainy",
            "Partly Cloudy"
        ]

        weather = random.choice(weather_options)
        speed_multiplier = round(random.uniform(0.8, 1.2), 2)

        rows.append({
            "train_number": train_number,
            "train_name": train_name,
            "current_station": current_station,
            "station_index": station_index,
            "delay_minutes": delay,
            "weather": weather,
            "speed_multiplier": speed_multiplier
        })

    with open("train_data_live.csv", "w", newline="") as file:
        fieldnames = [
            "train_number",
            "train_name",
            "current_station",
            "station_index",
            "delay_minutes",
            "weather",
            "speed_multiplier"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Sample train data generated successfully!")
    print(f"Number of trains: {len(rows)}")


if __name__ == "__main__":
    generate_sample_data()