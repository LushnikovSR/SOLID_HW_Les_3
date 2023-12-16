from abc import ABC, abstractmethod


class IShape3D(ABC):
    @abstractmethod
    def volume(self):
        pass