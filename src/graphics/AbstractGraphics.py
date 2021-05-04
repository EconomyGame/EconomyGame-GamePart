class AbstractGraphics:

    class GUI:
        pass

    class TextGUI(GUI):
        pass

    class ButtonGUI(GUI):
        pass

    class InputGUI(GUI):
        pass

    # create GUI
    def createTextGUI(self, x, y, text, color, size=100):
        return self.TextGUI()

    def createButtonGUI(self, x, y, width, height, label, callback):
        return self.ButtonGUI()

    def createInputGUI(self, x, y, width, height, callback):
        return self.InputGUI()

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
