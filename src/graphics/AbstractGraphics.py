class AbstractGraphics:

    class GUI:
        pass

    class TextGUI(GUI):
        pass

    class ButtonGUI(GUI):
        pass

    # create GUI
    def createTextGUI(self, x, y, text, color):
        return self.TextGUI()

    def createButtonGUI(self):
        return self.ButtonGUI()

    def __init__(self, width, height):
        pass

    def set_caption(self, caption: str):
        pass

    def set_fps(self, fps: int):
        pass

    def update_cycle(self):
        pass

    def get_events(self):
        pass

    def quit(self):
        pass

    def fill_screen(self, color):
        pass
