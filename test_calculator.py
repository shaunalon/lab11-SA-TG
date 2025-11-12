import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(4, 3), 5)
        self.assertAlmostEqual(hypotenuse(-2, 2), math.sqrt(8))
        self.assertAlmostEqual(hypotenuse(-1, -2), math.sqrt(5))

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
        with self.assertRaises(ValueError):
            square_root(-3)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()