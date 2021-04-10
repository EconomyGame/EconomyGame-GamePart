from . import AbstractScreen
import src.config as config


class Menu(AbstractScreen):

    def __init__(self, game):
        super().__init__(game)
        self.set_gui()

    def set_gui(self):
        self.objects.append(self.graphics.createTextGUI(300, 100, "Меню", config.MENU_TEXT_COLOR))

    def update(self):
        pass

    def render(self):
        self.graphics.fill_screen(config.MENU_BACKGROUND_COLOR)
        super().render()
