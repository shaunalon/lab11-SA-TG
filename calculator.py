import math

# First example
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
    if b <=1:
        raise ValueError("Base must be larger than 1.")
    if a == 0:
        raise ValueError("Argument cannot be 0")
    return math.log(b, a)

def exp(a,b):
    return math.pow(a,b)
