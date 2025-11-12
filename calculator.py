import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("Cannot take teh square root of a negative number.")

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b):
    return  a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ValueError("Division by 0")
    return b/a

def log(a,b):
    if b <= 0 or b == 1:
        raise ValueError("Base must be greater than 0 and not equal to 1.")
    if a <= 0:
        raise ValueError("Argument must be greater than 0")
    return math.log(b, a)

def exp(a,b):
    return math.pow(a,b)
