class AbstractObject:

    def __init__(self, game, x, y, path_to_image="static/img/default.png"):
        self.game = game
        self.x = x
        self.y = y
        self.path_to_image = path_to_image

    def render(self):
        self.game.graphics.draw_image(*self.game.get_absolute(self.x, self.y), self.path_to_image)

    def update(self):
        pass
