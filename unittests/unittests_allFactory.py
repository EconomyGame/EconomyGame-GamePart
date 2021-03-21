import unittest
from unittests.unittests_CityFactory import CityFactoryTest
from unittests.unittests_FactoryFactory import FactoryFactoryTest
from unittests.unittests_SourceFactory import SourceFactoryTest
from unittests.unittests_game import GameTest



class Test(unittest.TestCase):
    #Factory
    CityFactoryTest().test_type()
    FactoryFactoryTest().test_type()
    SourceFactoryTest().test_type()
    #Game
    GameTest().test_type()
    GameTest().test_memory()


if __name__ == '__main__':
    unittest.main()
