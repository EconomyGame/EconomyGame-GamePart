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

    def _build_factory_coal(self):
        self._build_factory(3)

    def _build_factory_gold(self):
        self._build_factory(2)

    def _build_factory_iron(self):
        self._build_factory(1)

    def _build_factory_diamond(self):
        self._build_factory(4)

    def _build_factory(self, res_id):
        if self.current_cell is None:
            return
        self.game.api.make_factory(self.game.my_username, res_id, self.current_cell)

    def _handle_connect_city(self, data):
        if self.current_cell is None:
            return
        obj = self.game.map[self.current_cell[0]][self.current_cell[1]]
        if not isinstance(obj, Factory):
            return
        x, y = map(int, data.split())
        city_id = self.game.map[x][y]._id
        self.game.api.select_city(self.game.my_username, obj._id, city_id)

    def _handle_connect_source(self, data):
        if self.current_cell is None:
            return
        obj = self.game.map[self.current_cell[0]][self.current_cell[1]]
        if not isinstance(obj, Factory):
            return
        x, y = map(int, data.split())
        source_id = self.game.map[x][y]._id
        self.game.api.select_source(self.game.my_username, obj._id, source_id)

    def set_gui(self):
        self.objects.append(self.graphics.createTexListGUI(450, 430, [], (255, 255, 255), 20))
        self.objects.append(self.graphics.createButtonGUI(50, 430, 90, 30, "Coal", self._build_factory_coal))
        self.objects.append(self.graphics.createTextGUI(50, 575, "$0", (255, 255, 255), 30))
        self.objects.append(self.graphics.createTextGUI(50, 480, "Подключение к городу", (255, 255, 255), 25))
        self.objects.append(self.graphics.createInputGUI(280, 480, 70, 30, self._handle_connect_city))
        self.objects.append(self.graphics.createTextGUI(50, 520, "Подключение к источнику", (255, 255, 255), 25))
        self.objects.append(self.graphics.createInputGUI(280, 520, 70, 30, self._handle_connect_source))
        self.objects.append(self.graphics.createButtonGUI(140, 430, 90, 30, "Gold", self._build_factory_gold))
        self.objects.append(self.graphics.createButtonGUI(230, 430, 90, 30, "Iron", self._build_factory_iron))
        self.objects.append(self.graphics.createButtonGUI(320, 430, 90, 30, "Diamond", self._build_factory_diamond))

    def update(self):
        self.objects[2].set_text(f"${self.game.balance}")

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
                elif isinstance(obj, Factory):
                    self.graphics.display_text(i * 40, j * 40, "F", (255, 255, 255))
        super().render()

    # Handlers
    def handle_mouse_click(self, x, y):
        super().handle_mouse_click(x, y)
        if y > 400:
            pass
            # self.current_cell = None
            # self.objects[0].set_texts([])
        else:
            self.current_cell = (x // 40, y // 40)
            obj = self.game.map[x // 40][y // 40]
            if isinstance(obj, City):
                self.objects[0].set_texts([f"Город {obj.name}", f"ID: {obj._id}", f"Coords: {obj.x} {obj.y}",
                                           f"Coal: Level {obj.resource_levels['coal']}, Stage: {obj.resource_stage['coal']}, Delta: {round(obj.resource_delta['coal'], 2)}",
                                           f"Gold: Level {obj.resource_levels['gold']}, Stage: {obj.resource_stage['gold']}, Delta: {round(obj.resource_delta['gold'], 2)}",
                                           f"Diamond: Level {obj.resource_levels['diamond']}, Stage: {obj.resource_stage['diamond']}, Delta: {round(obj.resource_delta['diamond'], 2)}",
                                           f"Iron: Level {obj.resource_levels['iron']}, Stage: {obj.resource_stage['iron']}, Delta: {round(obj.resource_delta['iron'], 2)}"
                                           ])
            elif isinstance(obj, Source):
                self.objects[0].set_texts([f"Ресурс {self.game.get_resource_name(obj.res_id)}", f"ID: {obj._id}", f"Coords: {obj.x} {obj.y}",
                                           f"Остаток: {obj.remain}"
                                           ])
            elif isinstance(obj, Factory):
                self.objects[0].set_texts([f"Фабрика игрока {obj.username}", f"ID: {obj._id}", f"Coords: {obj.x} {obj.y}",
                                           f"Ресурс: {self.game.get_resource_name(obj.resource_id)}",
                                           f"Уровень: {obj.level}",
                                            f"City id: {obj.city_id}", f"Source id: {obj.source_id}"])
            else:
                self.objects[0].set_texts(["Пустая клетка"])
