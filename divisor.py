# Can you find a range value that is a square, such that len(d1) is a power of two?

from collections import defaultdict
from math import floor, sqrt

def is_power_of_2(n):
    return (n != 0) and n & (n - 1) == 0
    
def factor_gen(n):
    return set(reduce(list.__add__, ([i, n/i] for i in range(1, int(sqrt(n) + 1)) if n % i == 0)))

for square_size in range(1, 1000):
    d1 = defaultdict(int)
    for i in range(1, square_size**2):
        d1[sum(factor_gen(i))] += 1

    print square_size**2, len(d1), is_power_of_2(len(d1))
