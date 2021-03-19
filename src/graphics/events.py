# Constants
BASIC_EVENT = 0
QUIT_EVENT = 0
KEY_DOWN_EVENT = 0
MOUSE_CLICK_EVENT = 0


class BasicEvent:

    type = BASIC_EVENT


class QuitEvent(BasicEvent):

    type = QUIT_EVENT


class KeyDownEvent(BasicEvent):

    type = KEY_DOWN_EVENT

    def __init__(self, key):
        self.key = key


class MouseClickEvent(BasicEvent):

    type = MOUSE_CLICK_EVENT

    def __init__(self, x, y):
        self.x = x
        self.y = y
