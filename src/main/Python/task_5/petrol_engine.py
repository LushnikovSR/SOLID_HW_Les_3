from engine import Engine


class PetrolEngine(Engine):
    model: str

    def __init__(self, model):
        self.model = model

    def start(self):
        pass
