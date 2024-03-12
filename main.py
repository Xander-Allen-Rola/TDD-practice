import unittest
import math

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10,0)

    def test_subtract(self):
        self.assertEqual(subtract(3,2), 1)

    def test_power(self):
        self.assertEqual(power(2,3),8)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("division by zero")
    return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def log(x, y):
    return math.log(x, y)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def ceil(x):
    return math.ceil(x)

def floor(x):
    return math.floor(x)

def exp(x):
    return math.exp(x)

def degrees(x):
    return math.degrees(x)

def radians(x):
    return math.radians(x)

# Additional functions
def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def isinf(x):
    """Checks if a number is positive or negative infinity."""
    return math.isinf(x)

def isnan(x):
    """Checks if a number is Not a Number (NaN)."""
    return math.isnan(x)

if __name__ == '__main__':
    unittest.main()

