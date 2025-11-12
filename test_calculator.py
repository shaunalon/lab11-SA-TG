# https://github.com/newmanhw/lab11-swe
# Partner 1: Shaun Alon
# Partner 2: Thaveesh Gallage

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(5, -1), 6)
        self.assertEqual(subtract(0, 0), 0)


    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5, 10), 50)
        self.assertEqual(mul(5, -3), -15)
        self.assertEqual(mul(-2, -1.5), 3.0)
    def test_divide(self): # 3 assertions
        self.assertEqual(div(50,5), 10)
        self.assertAlmostEqual(div(10, 4), 2.5)
        self.assertEqual(div(45, -9), -5)
# ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)


    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(4, 3), 5)
        self.assertAlmostEqual(hypotenuse(-2, 2), math.sqrt(8))
        self.assertAlmostEqual(hypotenuse(-1, -2), math.sqrt(5))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-3)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(1), 1)

    ##########################
# Do not touch this
if __name__ == "__main__":
    unittest.main()