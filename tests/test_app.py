# tests/test_app.py

import unittest
from src.app import add, subtract

class TestAppFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)

if __name__ == "__main__":
    unittest.main()
