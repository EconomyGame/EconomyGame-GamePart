from src.graphics import AbstractGraphics


class Game:

    def __init__(self, graphics: AbstractGraphics):
        self.graphics = graphics

    def update(self):
        pass

    def render(self):
        pass
