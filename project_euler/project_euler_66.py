#!/usr/bin/python

# http://mathworld.wolfram.com/PellEquation.html

from math import sqrt
from math import e
from mpmath import *
mp.prec = 242

def continuedFractionExpansion(f,n = 1): 
    assert(0.0 < f)
    a = int(f)
    x = f - a
    acfs = [a]
    for i in range(0,n):
        a = int(1.0 / x)
        x = 1.0 / x - a
        acfs.append(a)
    
    return acfs

acfs = continuedFractionExpansion(sqrt(2), 4)
assert(acfs == [1,2,2,2,2]) # [1;2,2,2,2]

def continuedFractionConvergents(acfs): 
    ps = [0,1]
    qs = [1,0]
    cs = [0.0,0.0]
    for i in range(0,len(acfs)):
        ps.append(acfs[i] * ps[-1] + ps[-2])
        qs.append(acfs[i] * qs[-1] + qs[-2])
        cs.append(ps[-1] / qs[-1])
    return {'p':ps,'q':qs,'p/q':cs}

acfs = continuedFractionExpansion(e, 20)
acfs0 = [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14]
assert(acfs == acfs0) # The final convergent is wrong, because 11 != 14.
continuedFractionConvergents(acfs)['p/q'][-1] == 2.718281828459045

def minimalSolution(n): 
    f = sqrt(mpf(str(n)))
    ps = [0,1]
    qs = [1,0]
    a = int(f)
    x = f - a
    p = a * ps[-1] + ps[-2]
    q = a * qs[-1] + qs[-2]
    if p * p - n * q * q == 1:
        return p
    ps.append(p)
    qs.append(q)
    ps.pop(0)
    qs.pop(0)
    while True:
        a = int(mpf(1.0) / x)
        x = mpf(1.0) / x - a
        p = a * ps[-1] + ps[-2]
        q = a * qs[-1] + qs[-2]
        if p * p - n * q * q == 1:
            return p
        ps.append(p)
        qs.append(q)
        ps.pop(0)
        qs.pop(0)

assert(minimalSolution(2) == 3)
assert(minimalSolution(3) == 2)
assert(minimalSolution(5) == 9)
assert(minimalSolution(7) == 8)
assert(minimalSolution(313) == 32188120829134849)
assert(minimalSolution(661) == 16421658242965910275055840472270471049)

# Main

maximum = 0
argMaximum = 0
m = 2
for n in range(2,1001):
    if m * m == n:
        m += 1
        continue
    minimalSolution0 = minimalSolution(n)
    if maximum < minimalSolution0:
        maximum = minimalSolution0
        argMaximum = n

assert(argMaximum == 661)
