from . import AbstractScreen
import src.config as config
from src.GameObjects import City, Factory, Source


class GameScreen(AbstractScreen):

    def __init__(self, game):
        super().__init__(game)
        self.current_cell = None
        self.set_gui()

    def empty(self, *args):
        pass

    def set_gui(self):
        self.objects.append(self.graphics.createTexListGUI(500, 430, [], (255, 255, 255)))
        self.objects.append(self.graphics.createButtonGUI(50, 430, 200, 30, "Построить фабрику", self.empty))

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
        # Draw symbols
        for i in range(20):
            for j in range(10):
                obj = self.game.map[i][j]
                if obj is None:
                    continue
                if isinstance(obj, City):
                    self.graphics.display_text(i * 40, j * 40, "C", (255, 255, 255))
                elif isinstance(obj, Source):
                    self.graphics.display_text(i * 40, j * 40, "S", (255, 255, 255))
        super().render()

    # Handlers
    def handle_mouse_click(self, x, y):
        if y > 400:
            self.current_cell = None
            self.objects[0].set_texts(["Пустая клетка"])
        else:
            self.current_cell = (x // 40, y // 40)
            obj = self.game.map[x // 40][y // 40]
            if isinstance(obj, City):
                self.objects[0].set_texts([f"Город {obj.name}"])
            elif isinstance(obj, Source):
                self.objects[0].set_texts([f"Ресурс"])
        super().handle_mouse_click(x, y)
