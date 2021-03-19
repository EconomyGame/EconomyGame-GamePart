from src.graphics import AbstractGraphics


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Game(metaclass=Singleton):  # Singleton class

    def __init__(self, graphics: AbstractGraphics = None):
        self.graphics = graphics

    def update(self):
        pass

    def render(self):
        pass

    def handle_key_down(self, key):
        pass

    def handle_mouse_click(self, x, y):
        pass
