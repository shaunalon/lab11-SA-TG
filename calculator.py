# https://github.com/newmanhw/lab11-swe
# Partner 1: Shaun Alon
# Partner 2: Thaveesh Gallage

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise
def hypotenuse(a,b):
    return math.hypot(a,b)

def subtract(a, b):
    return a - b

def div(a, b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def exp(a, b):
    return a**b

def add(a, b): 
    return  a+b

def mul(a,b):
    return a*b

def logarithm(a,b):
    if b <= 0 or b == 1:
        raise ValueError("Base must be greater than 0 and not equal to 1.")
    if a <= 0:
        raise ValueError("Argument must be greater than 0")
    return math.log(b, a)
