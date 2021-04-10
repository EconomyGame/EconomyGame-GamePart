from src.graphics import AbstractGraphics


class AbstractScreen:

    def __init__(self, game):
        self.game = game
        self.objects = []
        self.graphics: AbstractGraphics = game.graphics

    def update(self):
        pass

    def render(self):
        for obj in self.objects:
            obj.render()
