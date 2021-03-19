import unittest
from reverse import reverse

class TestReverse(unittest.TestCase):
    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)

if __name__ == '__main__':
    unittest.main()