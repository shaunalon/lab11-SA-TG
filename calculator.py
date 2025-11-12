import math


import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def log(a, b):
    if a<=0 or b<=0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(b,a)# use math library + raise ValueError

def exp(a, b):
    return a**b

def add(a, b): 
    return  a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b


def log(a,b):
    if b <=1:
        raise ValueError("Base must be larger than 1.")
    if a == 0:
        raise ValueError("Argument cannot be 0")
    return math.log(b, a)

def exp(a,b):
    return math.pow(a,b)
