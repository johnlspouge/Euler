#!/usr/bin/python

import math

factors = []

# Returns true if none of the "primes" divides n.
def Is_Prime(primes, n):

    for p in primes:
        if n % p == 0:
            return False;

    return True;

n = int(input("prime of cardinality: "))

primes = []

p = 2
while len(primes) < n:
    if Is_Prime(primes, p):
        primes.append(p)
    p += 1

print(primes[-1])