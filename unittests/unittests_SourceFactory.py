import unittest
from src.GameObjects import SourceFactory
from src.GameObjects import AbstractObject
from src.graphics import AbstractGraphics
from src.game import Game


class SourceFactoryTest(unittest.TestCase):

    def test_type(self):
        graphics = AbstractGraphics(0, 0)
        game = Game(graphics)
        self.assertEqual(isinstance(SourceFactory(game).create_source(0, 0), AbstractObject), True)


if __name__ == '__main__':
    unittest.main()
