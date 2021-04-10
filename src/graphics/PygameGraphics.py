import pygame
import src.config as config
from src.graphics.AbstractGraphics import AbstractGraphics
from .events import *


class PygameGraphics(AbstractGraphics):

    class GUI:

        def __init__(self, screen, x, y, width, height):
            self.screen = screen
            self.x = x
            self.y = y
            self.width = width
            self.height = height

        def render(self):
            pass

    class TextGUI(GUI):

        def __init__(self, screen, x, y, width, height, text, color):
            self.font = pygame.font.Font(config.TEXT_FONT, 100)
            self.label = self.font.render(text, True, color)
            super().__init__(screen, x, y, width, height)

        def render(self):
            self.screen.blit(self.label, (self.x, self.y))

        def handle_click(self, pos_x, pos_y):
            pass

    class ButtonGUI(GUI):

        def __init__(self, screen, x, y, width, height, label):
            self.label = label
            super().__init__(screen, x, y, width, height)

        def render(self):
            pass

        def handle_click(self, pos_x, pos_y):
            pass

    # create GUI
    def createTextGUI(self, x, y, text, color):
        return self.TextGUI(self._screen, x, y, 0, 0, text, color)

    def createButtonGUI(self):
        pass

    def __init__(self, width, height):
        pygame.init()
        self._screen = pygame.display.set_mode((width, height))
        self._timer = pygame.time.Clock()
        self.fps = 30
        super().__init__(width, height)

    def set_caption(self, caption: str):
        pygame.display.set_caption(caption)

    def set_fps(self, fps: int):
        self.fps = fps

    def update_cycle(self):
        pygame.display.flip()
        self._timer.tick(self.fps)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                yield QuitEvent()
            elif event.type == pygame.KEYDOWN:
                yield KeyDownEvent(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                yield MouseClickEvent(*event.pos)

    def quit(self):
        pygame.quit()

    def fill_screen(self, color):
        self._screen.fill(color)
