from math import gcd
from functools import reduce
def solution(arr):
    return reduce(lambda x, y: x * y // gcd(x, y), arr)