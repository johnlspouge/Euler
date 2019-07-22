#!/usr/bin/python

from euler import appendToPrimes, primeFactors, primePowerFactorization

PRIMES = []
UPPER = 10**6
appendToPrimes(UPPER, PRIMES)

m = 2 # current test
foursome = 0 
while foursome != m:
    foursome = m
    for j in range(m,m+4):
        dict = primePowerFactorization(primeFactors(j, PRIMES))
        if len(dict.keys()) != 4:
            m = j + 1
            break

print(foursome)    
