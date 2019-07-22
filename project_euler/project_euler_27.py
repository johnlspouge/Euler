#!/usr/bin/python

import euler

BOUND = 1000 # upper bound for testing primalities
TERMS = 3 # terms in quadratic
primes = set(euler.appendToPrimes(TERMS * BOUND * BOUND))
            
def quadratic(n, a, b):
    return n * n + a * n + b

def isPrime(n, a, b, primes):
    return quadratic(n, a, b) in primes

# Returns the count of prime values starting from n = 0.
def countOfPrimes(maximum, a, b, primes):
    n = 0
    while n <= maximum:
        if isPrime(n, a, b, primes):
            n += 1
        else:
            return n
    
maximumCount = 0 # max counter for primes

a = -BOUND + 1
while a < BOUND - 1:
    b = -BOUND
    while b <= BOUND:
        count = countOfPrimes(BOUND * BOUND, a, b, primes)
        if maximumCount < count:
            maxA = a
            maxB = b
            maximumCount = count
        b += 1
    a += 1

#print(countOfPrimes(100, -79, 1601, primes))                
print(maxA, maxB, maxA * maxB)                
