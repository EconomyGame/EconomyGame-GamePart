from src.graphics import AbstractGraphics
from src.screens import Menu


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Game(metaclass=Singleton):  # Singleton class
    def __init__(self, graphics: AbstractGraphics = None):
        self.graphics = graphics
        self.current_screen = Menu(self)

    def update(self):
        self.current_screen.update()

    def render(self):
        self.current_screen.render()

    def set_new_screen(self, screen):
        self.current_screen = screen

    def handle_key_down(self, event):
        self.current_screen.handle_key_down(event)

    def handle_mouse_click(self, x, y):
        self.current_screen.handle_mouse_click(x, y)
