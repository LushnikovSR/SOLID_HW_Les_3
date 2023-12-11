from engine import Engine


class Car(Engine):
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()
