#!/usr/bin/python

from euler import readPrimes

primes = readPrimes( 10**6 ) 

pr0 = 1
for p in primes:
    pr = p * pr0
    if pr > 10**6:
        break
    pr0 = pr
    
print( pr0 )