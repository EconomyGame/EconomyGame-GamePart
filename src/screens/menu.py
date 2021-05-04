from . import AbstractScreen, Waiting
import src.config as config


class Menu(AbstractScreen):

    def __init__(self, game):
        super().__init__(game)
        self.set_gui()

    def _create_game(self):
        self.game.current_screen = Waiting(self.game)

    def _join_game(self):
        print("JOINED")

    def set_gui(self):
        self.objects.append(self.graphics.createTextGUI(300, 100, "Меню", config.MENU_TEXT_COLOR))
        self.objects.append(self.graphics.createButtonGUI(315, 200, 145, 30, "Создать игру", self._create_game))
        self.objects.append(self.graphics.createButtonGUI(290, 250, 225, 30, "Подключиться к игре", self._join_game))

    def update(self):
        pass

    def render(self):
        self.graphics.fill_screen(config.MENU_BACKGROUND_COLOR)
        super().render()

    # Handlers
    def handle_mouse_click(self, x, y):
        super().handle_mouse_click(x, y)
