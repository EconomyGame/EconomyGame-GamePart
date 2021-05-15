from src.screens import AbstractScreen, GameScreen
import src.config as config


class Waiting(AbstractScreen):

    def __init__(self, game):
        super().__init__(game)
        self.set_gui()

    def _start_game(self):
        self.game.api.start_game(self.game.my_username)
        self.game.current_screen = GameScreen(self.game)

    def set_gui(self):
        self.objects.append(self.graphics.createTextGUI(150, 100, "Зал ожидания", config.MENU_TEXT_COLOR))
        self.objects.append(self.graphics.createTextGUI(150, 200, f"Другие игроки могут подключиться по коду: {self.game.ref_code}", config.MENU_TEXT_COLOR, size=30))
        self.objects.append(self.graphics.createTexListGUI(150, 300, [], config.MENU_TEXT_COLOR))
        self.objects.append(self.graphics.createButtonGUI(300, 300, 150, 30, "Начать игру", self._start_game))
        # self.objects.append(self.graphics.createButtonGUI(315, 200, 145, 30, "Создать игру", create_game))
        # self.objects.append(self.graphics.createButtonGUI(290, 250, 225, 30, "Подключиться к игре", join_game))

    def update(self):
        self.objects[1].set_text(f"Другие игроки могут подключиться по коду: {self.game.ref_code}")
        self.objects[2].set_texts(self.game.users)
        if len(self.game.users) == 4 and len(self.objects) < 4:
            self.objects.append(self.graphics.createButtonGUI(300, 300, 150, 30, "Начать игру", self._start_game))

    def render(self):
        self.graphics.fill_screen(config.MENU_BACKGROUND_COLOR)
        super().render()

    # Handlers
    def handle_mouse_click(self, x, y):
        super().handle_mouse_click(x, y)
