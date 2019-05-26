#!/usr/bin/python

import math

factors = []

# Returns true if none of the "primes" divides n.
def Is_Prime(primes, n):

    for p in primes:
        if p * p > n:
            return True
        elif n % p == 0:
            return False;

    return True;

n = int(input("exclusive upper bound: "))

primes = []

sum = 0
p = 2
while p < n:
    if Is_Prime(primes, p):
        primes.append(p)
        sum += p
    p += 1

print(sum)