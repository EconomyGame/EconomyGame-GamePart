from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

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

        def __init__(self, screen, x, y, width, height, text, color, size=100):
            self.font = pygame.font.Font(config.TEXT_FONT, size)
            self.label = self.font.render(text, True, color)
            self.text = text
            self.color = color
            super().__init__(screen, x, y, width, height)

        def render(self):
            self.screen.blit(self.label, (self.x, self.y))

        def set_text(self, text):
            if text == self.text:
                return
            self.text = text
            self.label = self.font.render(text, True, self.color)

        def handle_click(self, pos_x, pos_y):
            pass

        def handle_key_down(self, event):
            pass

    class TextListGUI(GUI):

        def __init__(self, screen, x, y, width, height, text_list, color, size):
            self.color = color
            self.size = size
            self.texts = []
            current_y = y
            for text in text_list:
                self.texts.append(PygameGraphics.TextGUI(screen, x, current_y, 0, 0, text, color, size))
                current_y += 20
            super().__init__(screen, x, y, width, height)

        def set_texts(self, text_list):
            if self.texts == text_list:
                return
            if len(self.texts) == len(text_list):
                for i, text in enumerate(self.texts):
                    text.set_text(text_list[i])
                return
            self.texts = []
            current_y = self.y
            for text in text_list:
                self.texts.append(PygameGraphics.TextGUI(self.screen, self.x, current_y, 0, 0, text, self.color, self.size))
                current_y += 20

        def render(self):
            for text in self.texts:
                text.render()

        def handle_click(self, pos_x, pos_y):
            pass

        def handle_key_down(self, event):
            pass

    class ButtonGUI(GUI):

        def __init__(self, screen, x, y, width, height, label, callback):
            self.label = label
            self.callback = callback
            self.font = pygame.font.Font(config.TEXT_FONT, 30)
            self.label_obj = self.font.render(label, True, config.BUTTON_TEXT_COLOR)
            super().__init__(screen, x, y, width, height)

        def render(self):
            pygame.draw.rect(self.screen, config.BUTTON_BODY_COLOR, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(self.screen, config.BUTTON_BORDER_COLOR, (self.x, self.y, self.width, self.height), 3)
            self.screen.blit(self.label_obj, (self.x + 4, self.y + 4))

        def handle_click(self, pos_x, pos_y):
            if self.x <= pos_x <= self.x + self.width and self.y <= pos_y <= self.y + self.height:
                self.callback()

        def handle_key_down(self, event):
            pass

    class InputGUI(GUI):

        def __init__(self, screen, x, y, width, height, callback):
            self.callback = callback
            self.text = ""
            self.font = pygame.font.Font(config.TEXT_FONT, 26)
            self.text_obj = self.font.render(self.text, True, config.INPUT_TEXT_COLOR)
            self.active = False
            super().__init__(screen, x, y, width, height)

        def render(self):
            pygame.draw.rect(self.screen, config.INPUT_BODY_COLOR, (self.x, self.y, self.width, self.height))
            if self.active:
                pygame.draw.rect(self.screen, config.INPUT_BORDER_COLOR, (self.x, self.y, self.width, self.height), 3)
            self.screen.blit(self.text_obj, (self.x + 4, self.y + 4))

        def handle_click(self, pos_x, pos_y):
            if self.x <= pos_x <= self.x + self.width and self.y <= pos_y <= self.y + self.height:
                self.active = True
            else:
                self.active = False

        def handle_key_down(self, event):
            if not self.active:
                return
            if event.key == pygame.K_RETURN:
                self.callback(self.text)
            elif event.key == pygame.K_BACKSPACE:
                if self.text:
                    self.text = self.text[:-1]
                    self.text_obj = self.font.render(self.text, True, config.INPUT_TEXT_COLOR)
            else:
                self.text += event.unicode
                self.text_obj = self.font.render(self.text, True, config.INPUT_TEXT_COLOR)

    # create GUI
    def createTextGUI(self, x, y, text, color, size=100):
        return self.TextGUI(self._screen, x, y, 0, 0, text, color, size=size)

    def createTexListGUI(self, x, y, text_list, color, size=30):
        return self.TextListGUI(self._screen, x, y, 0, 0, text_list, color, size=30)

    def createButtonGUI(self, x, y, width, height, label, callback):
        return self.ButtonGUI(self._screen, x, y, width, height, label, callback)

    def createInputGUI(self, x, y, width, height, callback):
        return self.InputGUI(self._screen, x, y, width, height, callback)

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
                yield KeyDownEvent(event.key, event.unicode)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                yield MouseClickEvent(*event.pos)

    def quit(self):
        pygame.quit()

    def fill_screen(self, color):
        self._screen.fill(color)

    def draw_line(self, color, start_pos, end_pos):
        pygame.draw.line(self._screen, color, start_pos, end_pos)

    def draw_rect(self, color, x, y, width, height):
        pygame.draw.rect(self._screen, color, (x, y, width, height))
