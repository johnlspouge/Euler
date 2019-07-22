#!/usr/bin/python

from itertools import permutations 
from euler import appendToPrimes

BASE = 10

PRIMES = []
appendToPrimes(18, PRIMES)
assert(PRIMES[-1] == 17)
assert(len(PRIMES) == BASE - 3)

def isSubstringDivisible(n):
    for i in range(1, BASE - 2):
        triple = n % (BASE ** 3)
        if triple % PRIMES[-i] != 0:
            return False
        n //= BASE
    return True
    
strings = list(permutations(range(0,BASE)))
pandigitals = [int(''.join(map(str, s))) for s in strings]

print(sum([n for n in pandigitals if isSubstringDivisible(n)]))
