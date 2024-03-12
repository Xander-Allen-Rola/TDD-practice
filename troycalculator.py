import unittest
import math

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        
    def test_subtract(self):
        self.assertEqual(subtract(6, 2), 4)
        
    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)
        
    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        self.assertEqual(divide(6, 3), 2)
        self.assertNotEqual(divide(7, 2), 4)
    
    def test_power(self):
        self.assertEqual(power(6, 2), 36)
        
    def test_sqrt(self):
        self.assertEqual(sqrt(9), 3)
        self.assertAlmostEqual(sqrt(26), 5.09901951359)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y==0:
        raise ZeroDivisionError("division by zero")
    return x / y

def power(x, y):
    return x**y

def sqrt(x):
    return math.sqrt(x)

if __name__ == '__main__':
    unittest.main()