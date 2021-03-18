from src.GameObjects.AbstractObject import AbstractObject


class CityFactory:

    def __init__(self, game):
        self.game = game

    def create_source(self, x, y):
        return AbstractObject(self.game, x, y, path_to_image="static/img/city.png")
