import math


def comb(a: int, b: int):
    return int(math.factorial(a) / (math.factorial(b) * math.factorial(a - b)))
