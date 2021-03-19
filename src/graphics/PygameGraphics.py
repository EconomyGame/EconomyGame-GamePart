from src.graphics.AbstractGraphics import AbstractGraphics
import pygame
from .events import *


class PygameGraphics(AbstractGraphics):
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
