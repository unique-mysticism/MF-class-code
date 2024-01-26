import unittest
from myadd import add

class MainTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2,3))

if __name__ == "__main__":
    unittest.main()
