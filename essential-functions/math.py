import math


def square(num):
    if type(num) != int:
        raise Exception("Input must be a number.")
    return math.sqrt(num)

