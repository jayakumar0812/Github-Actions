import unittest
from calculator import Calculator

class TestCalculatorAdvanced(unittest.TestCase):
    """Tests for advanced scenarios in the Calculator class."""

    def setUp(self):
        """Set up a Calculator instance for testing."""
        self.calc = Calculator()

    def test_add_with_floats(self):
        self.assertAlmostEqual(self.calc.add(1.1, 2.2), 3.3)
        self.assertAlmostEqual(self.calc.add(-0.1, 0.1), 0.0)

    def test_subtract_with_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertAlmostEqual(self.calc.subtract(-1.1, -0.9), -0.2)

    def test_large_numbers(self):
        self.assertEqual(self.calc.add(1_000_000_000, 2_000_000_000), 3_000_000_000)
        self.assertEqual(self.calc.subtract(10_000_000, 5_000_000), 5_000_000)

    def test_divide_with_floats(self):
        self.assertAlmostEqual(self.calc.divide(22.0, 7.0), 22.0 / 7.0)
        self.assertAlmostEqual(self.calc.divide(0.0, 1.0), 0.0)

if __name__ == "__main__":
    unittest.main()
