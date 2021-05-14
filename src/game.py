from src.graphics import AbstractGraphics
from src.interaction import Api, start_thread
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
        self.api = Api(self)
        start_thread(self.handle_update)
        self.map = [[None for _ in range(20)] for _ in range(10)]
        self.ref_code = ""
        self.users = []

    def update(self):
        self.current_screen.update()

    def render(self):
        self.current_screen.render()

    def handle_update(self, data):
        print(data)
        if "ref_code" in data:
            self.ref_code = data["ref_code"]
        else:
            self.ref_code = data["game"]["ref_code"]
        print(self.ref_code)
        self.users = []
        if "users" in data:
            users = data["users"]
        else:
            users = data["game"]["users"]
        for user in users:
            self.users.append(user["username"])


    def set_new_screen(self, screen):
        self.current_screen = screen

    def handle_key_down(self, event):
        self.current_screen.handle_key_down(event)

    def handle_mouse_click(self, x, y):
        self.current_screen.handle_mouse_click(x, y)
