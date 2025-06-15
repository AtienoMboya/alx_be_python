import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test the addition method"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4,-6), -10)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(15, 3), 12)
        self.assertEqual(self.calc.subtract(-4, -5), 1)
        self.assertEqual(self.calc.subtract(-4, 5), -9)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(15, 3), 45)
        self.assertEqual(self.calc.multiply(-4, -6), 24)
        self.assertEqual(self.calc.multiply(15, 0), 0)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(-15, -3), 5)