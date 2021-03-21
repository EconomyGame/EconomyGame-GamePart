import unittest
from src.graphics import AbstractGraphics
from src.game import Game


class GameTest(unittest.TestCase):

    def test_type(self):
        graphics = AbstractGraphics(0, 0)
        self.assertEqual(isinstance(Game(graphics), Game), True)

    def test_memory(self):
        graphics1 = AbstractGraphics(0, 0)
        graphics2 = AbstractGraphics(1, 1)
        self.assertEqual(Game(graphics1) is Game(graphics2), True)


if __name__ == '__main__':
    unittest.main()
