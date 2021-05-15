from src.graphics import AbstractGraphics
from src.interaction import Api, start_thread
from src.screens import Menu
import src.config as config
from src.GameObjects import City, Factory, Source


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
        self.map = [[None for _ in range(10)] for _ in range(20)]
        self.ref_code = ""
        self.users = []
        self.balance = 0
        self.profit_per_sec = 0

    def update(self):
        self.balance += self.profit_per_sec // config.FPS
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

    def progress_update(self, data):
        self.map = [[None for _ in range(10)] for _ in range(20)]
        for city in data["game"]["cities"]:
            self.map[city["coords"][0]][city["coords"][1]] = City(city["_id"], city["coords"][0], city["coords"][1],
                                                                  city["name"], city["resource_delta"],
                                                                  city["resource_levels"], city["resource_stage"])
        for source in data["game"]["sources"]:
            self.map[source["coords"][0]][source["coords"][1]] = Source(source["_id"], source["coords"][0], source["coords"][1],
                                                                        source["delta"], source["remain"], source["resource_id"])

    def set_new_screen(self, screen):
        self.current_screen = screen

    def handle_key_down(self, event):
        self.current_screen.handle_key_down(event)

    def handle_mouse_click(self, x, y):
        self.current_screen.handle_mouse_click(x, y)
