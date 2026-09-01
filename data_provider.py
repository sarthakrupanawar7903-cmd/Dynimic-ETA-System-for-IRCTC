# data_provider.py - Abstract Data Provider

from abc import ABC, abstractmethod


class DataProvider(ABC):
    """Abstract class for all data providers"""

    @abstractmethod
    def get_train_location(self, train_number):
        """Get current location of a train"""
        pass

    @abstractmethod
    def get_train_delay(self, train_number):
        """Get current delay of a train"""
        pass

    @abstractmethod
    def get_weather(self, station_code):
        """Get current weather at a station"""
        pass

    @abstractmethod
    def get_congestion_level(self, route):
        """Get congestion level on a route"""
        pass

    @abstractmethod
    def update_train_position(self, train_number, new_position):
        """Update a train's position"""
        pass