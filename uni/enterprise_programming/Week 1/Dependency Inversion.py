"""
Dependency inversion principle
Classes should depend on abstraction and not concrete implementations
"""

# Wrong

class FrontEnd:
    def __init__(self, backend):
        self.backend = backend

    def display_data(self):
        data = self.backend.fetch_data()
        print(data)

class Backend:
    def __init__(self, source):
        self.source = source

    def fetch_data(self):
        if self.source == "database":
            data = ["apple", "banana", "grape"]
            return data
        elif self.source == "API":
            pass


# Correct
from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.fetch_data()
        print(data)

class DataSource(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

class BackendDatabase(DataSource):
    def fetch_data(self):
        data = ["apple", "banana", "grape"]
        return data

class BackendAPI(DataSource):
    def fetch_data(self):
        data = {"name": "ABC", "age": 21}
        return data