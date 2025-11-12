import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sub(5, -1), 6)
        self.assertEqual(sub(0, 0), 0)


    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)


    def test_logarithm(self):
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(3, 9), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)


# Do not touch this
if __name__ == "__main__":
    unittest.main()