# mock_provider.py - Mock Data Provider

from data_provider import DataProvider
from app import TRAINS, WEATHER_DB, STATION_NAMES


class MockProvider(DataProvider):
    """Provides simulated data for testing"""

    def __init__(self):
        self.trains = TRAINS
        self.weather = WEATHER_DB
        self.position_updates = {}

    def get_train_location(self, train_number):
        """Get current location from train data"""

        for train in self.trains:
            if train['number'] == train_number:
                idx = train['current_station_index']

                return {
                    'station_code': train['route'][idx],
                    'station_name': STATION_NAMES.get(
                        train['route'][idx],
                        train['route'][idx]
                    ),
                    'index': idx
                }

        return None

    def get_train_delay(self, train_number):
        """Get current delay"""

        for train in self.trains:
            if train['number'] == train_number:
                return train['delay']

        return 0

    def get_weather(self, station_code):
        """Get current weather"""

        return self.weather.get(station_code, {})

    def get_congestion_level(self, route):
        """Get congestion level"""

        return "Medium"

    def update_train_position(self, train_number, new_position):
        """Update train position"""

        self.position_updates[train_number] = new_position
        return True