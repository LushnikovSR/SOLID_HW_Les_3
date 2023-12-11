from abc import ABC, abstractmethod


class Engine:
    model: str

    @abstractmethod
    def start(self):
        pass
