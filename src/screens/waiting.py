from src.screens import AbstractScreen
import src.config as config


class Waiting(AbstractScreen):

    def __init__(self, game):
        super().__init__(game)
        self.set_gui()

    def set_gui(self):
        self.objects.append(self.graphics.createTextGUI(150, 100, "Зал ожидания", config.MENU_TEXT_COLOR))
        self.objects.append(self.graphics.createTextGUI(150, 200, "Другие игроки могут подключиться по коду: kekseva", config.MENU_TEXT_COLOR, size=30))
        # self.objects.append(self.graphics.createButtonGUI(315, 200, 145, 30, "Создать игру", create_game))
        # self.objects.append(self.graphics.createButtonGUI(290, 250, 225, 30, "Подключиться к игре", join_game))

    def update(self):
        pass

    def render(self):
        self.graphics.fill_screen(config.MENU_BACKGROUND_COLOR)
        super().render()

    # Handlers
    def handle_mouse_click(self, x, y):
        super().handle_mouse_click(x, y)
