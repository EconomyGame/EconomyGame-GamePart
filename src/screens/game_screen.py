from . import AbstractScreen
import src.config as config


class GameScreen(AbstractScreen):

    def __init__(self, game):
        super().__init__(game)
        self.current_cell = None
        self.set_gui()

    def set_gui(self):
        pass

    def update(self):
        pass

    def render(self):
        self.graphics.fill_screen(config.MENU_BACKGROUND_COLOR)
        for i in range(0, 401, 40):
            self.graphics.draw_line((255, 255, 255), (0, i), (800, i))
        for j in range(0, 801, 40):
            self.graphics.draw_line((255, 255, 255), (j, 0), (j, 400))
        if self.current_cell is not None:
            self.graphics.draw_rect((255, 219, 139), self.current_cell[0] * 40, self.current_cell[1] * 40, 40, 40)
        super().render()

    # Handlers
    def handle_mouse_click(self, x, y):
        if y > 400:
            self.current_cell = None
        else:
            self.current_cell = (x // 40, y // 40)
        super().handle_mouse_click(x, y)
