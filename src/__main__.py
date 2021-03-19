from src.graphics import PygameGraphics
from src.game import Game
import src.config as config
from src.graphics.events import *


graphics = PygameGraphics(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
graphics.set_caption(config.WINDOW_CAPTION)
graphics.set_fps(config.FPS)

game = Game(graphics)

running = True
while running:
    # TODO events
    for event in graphics.get_events():
        if event.type == QUIT_EVENT:
            running = False  # TODO close connection, etc...
        elif event.type == KEY_DOWN_EVENT:
            game.handle_key_down(event.key)  # TODO handler of keys
        elif event.type == MOUSE_CLICK_EVENT:
            game.handle_mouse_click(event.x, event.y)
    graphics.fill_screen((0, 0, 0))
    game.update()
    game.render()
    graphics.update_cycle()

graphics.quit()
