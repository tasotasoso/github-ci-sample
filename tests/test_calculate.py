import unittest
from src import calculate

class TestCalculate(unittest.TestCase):
    """test class of calculate.py
    """

    def test_add(self):
        """test method for add
        """
        x1 = 2
        x2 = 1.5
        exp = 3.5
        res = calculate.add(x1, x2)
        self.assertEqual(exp, res)

    def test_subtract(self):
        """test method for subtract
        """
        x1 = 2.6
        x2 = 0.5
        exp = 2.1
        res = calculate.subtract(x1, x2)
        self.assertEqual(exp, res)