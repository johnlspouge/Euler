#!/usr/bin/python

from math import sqrt
from mpmath import *
mp.prec = 100

def continuedFractionExpansionPeriodLength(n): 
    assert(0 < n)
    f = sqrt(mpf(str(n)))
    a0 = int(f)
    if a0 * a0 == n or (a0 + 1) * (a0 + 1) == n:
        return 0 # adds 0 for perfect squares
    a = 0
    x = f - a0
    period = 0
    while a != 2 * a0:
        a = int(mpf("1.0") / x)
        x = 1.0 / x - a
        period += 1
    return period

assert(continuedFractionExpansionPeriodLength(2) == 1)
assert(continuedFractionExpansionPeriodLength(3) == 2)
assert(continuedFractionExpansionPeriodLength(5) == 1)
assert(continuedFractionExpansionPeriodLength(6) == 2)
assert(continuedFractionExpansionPeriodLength(7) == 4)
assert(continuedFractionExpansionPeriodLength(8) == 2)
assert(continuedFractionExpansionPeriodLength(10) == 1)
assert(continuedFractionExpansionPeriodLength(11) == 2)
assert(continuedFractionExpansionPeriodLength(12) == 2)
assert(continuedFractionExpansionPeriodLength(13) == 5)

# Main

assert(sum([continuedFractionExpansionPeriodLength(n) % 2 for n in range(2,14)]) == 4)
assert(sum([continuedFractionExpansionPeriodLength(n) % 2 for n in range(2,10000)]) == 1322) # mp.prec = 1000
# 1559 at mp.prec = 242