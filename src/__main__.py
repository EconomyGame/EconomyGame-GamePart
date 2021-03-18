from src.graphics.PygameGraphics import PygameGraphics
from src.game import Game
import src.config as config


graphics = PygameGraphics(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
graphics.set_caption(config.WINDOW_CAPTION)
graphics.set_fps(config.FPS)

game = Game(graphics)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            game.send_event(event)
    graphics.fill_screen((0, 0, 0))
    game.update()
    game.render()
    graphics.update_cycle()

graphics.quit()
