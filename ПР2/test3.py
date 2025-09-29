import unittest
from calc import calculate_expression, step_by_step_calculator

class TestCalculator(unittest.TestCase):
    def test_calculate_expression_valid(self):
        self.assertEqual(calculate_expression("10 + 5"), 15)
        self.assertEqual(calculate_expression("10 / 2"), 5)
        self.assertEqual(calculate_expression("2 * 3 + 1"), 7)
        self.assertEqual(calculate_expression("10 - 3 * 2"), 4)

    def test_calculate_expression_invalid(self):
        self.assertTrue("Error in expression" in calculate_expression("10 / 0"))
        self.assertTrue("Error in expression" in calculate_expression("10 +"))
        self.assertTrue("Error in expression" in calculate_expression("abc"))

if __name__ == '__main__':
    unittest.main()