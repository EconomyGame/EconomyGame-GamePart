from . import AbstractScreen, Waiting
import src.config as config


class JoinScreenCode(AbstractScreen):

    def __init__(self, game, name):
        super().__init__(game)
        self.name = name
        self.set_gui()

    def _join_game(self, code):
        self.game.api.join_game(self.name, code)
        self.game.current_screen = Waiting(self.game)

    def set_gui(self):
        self.objects.append(self.graphics.createTextGUI(200, 100, "Введите код", config.MENU_TEXT_COLOR))
        self.objects.append(self.graphics.createInputGUI(315, 200, 100, 30, self._join_game))

    def update(self):
        pass

    def render(self):
        self.graphics.fill_screen(config.MENU_BACKGROUND_COLOR)
        super().render()

    # Handlers
    def handle_mouse_click(self, x, y):
        super().handle_mouse_click(x, y)
