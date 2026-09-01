# csv_provider.py - CSV Data Provider

import pandas as pd
from data_provider import DataProvider
from app import STATION_NAMES


class CSVProvider(DataProvider):
    """Reads train data from CSV file."""

    def __init__(self, csv_path="train_data_live.csv"):
        self.df = pd.read_csv(csv_path) if csv_path else None
        self.current_positions = {}

    def load_data(self, csv_path):
        """Load data from CSV."""
        self.df = pd.read_csv(csv_path)
        return len(self.df)

    def get_train_location(self, train_number):
        """Get current location from CSV."""

        if self.df is None:
            return None

        row = self.df[self.df["train_number"] == train_number]

        if row.empty:
            return None

        station = row.iloc[0]["current_station"]

        return {
            "station_code": station,
            "station_name": STATION_NAMES.get(station, station),
            "index": row.iloc[0]["station_index"]
        }

    def get_train_delay(self, train_number):
        """Get delay from CSV."""

        if self.df is None:
            return 0

        row = self.df[self.df["train_number"] == train_number]

        if row.empty:
            return 0

        return int(row.iloc[0]["delay_minutes"])

    def get_weather(self, station_code):
        """Get weather from CSV."""

        if self.df is None:
            return None

        row = self.df[self.df["current_station"] == station_code]

        if row.empty:
            return None

        return row.iloc[0]["weather"]

    def get_congestion_level(self, route):
        """Get congestion level."""

        return "Medium"

    def update_train_position(self, train_number, new_position):
        """Update a train's position."""

        self.current_positions[train_number] = new_position
        return True