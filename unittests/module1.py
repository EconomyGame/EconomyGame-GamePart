import unittest
from reverse import reverse

class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

if __name__ == '__main__':
    unittest.main()
