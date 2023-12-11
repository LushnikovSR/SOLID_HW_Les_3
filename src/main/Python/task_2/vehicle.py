from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, max_speed, type):
        self.max_speed = max_speed
        self.type = type

    @abstractmethod
    def get_max_speed(self):
        pass

    @abstractmethod
    def get_type(self):
        pass
