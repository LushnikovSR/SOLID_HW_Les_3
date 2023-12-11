from abc import ABC, abstractmethod


class IShape2D(ABC):
    @abstractmethod
    def area(self):
        pass
