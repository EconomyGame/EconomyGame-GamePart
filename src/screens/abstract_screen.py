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

    #Handlers
    def handle_mouse_click(self, x, y):
        for obj in self.objects:
            obj.handle_click(x, y)

    def handle_key_down(self, event):
        for obj in self.objects:
            obj.handle_key_down(event)
