import unittest
from simple_calculator import SimpleCalculator

class Tests(unittest.TestCase):
    def test_add_positive(self):
        result = SimpleCalculator.add(self, 5, 3)
        self.assertEqual(result, 8)
    
    def test_add_negative(self):
        result = SimpleCalculator.add(self, -5, -3)
        self.assertEqual(result, -8)

    def test_subtract_positive(self):
        result = SimpleCalculator.subtract(self, 5, 3)
        self.assertEqual(result, 2)

    def test_subtract_negative(self):
        result = SimpleCalculator.subtract(self, -5, -3)
        self.assertEqual(result, -2)

    def test_multiply(self):
        result = SimpleCalculator.multiply(self, 5, 3)
        self.assertEqual(result, 15)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            SimpleCalculator.divide(self, 5, 0)
        
    def test_valid_division(self):
        result = SimpleCalculator.divide(self, 15, 5)
        self.assertEqual(result, 3)
