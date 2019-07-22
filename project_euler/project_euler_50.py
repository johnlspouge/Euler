#!/usr/bin/python

from euler import appendToPrimes
import time
from math import log

startTime = time.time()
PRIMES = []
UPPER = 10**6
appendToPrimes(UPPER, PRIMES)
PRIME_SET = set(PRIMES)
print("{:.3f}".format(time.time() - startTime))

print(len(PRIMES), "{:.3f}".format(len(PRIMES) / (UPPER/log(UPPER))))

startTime = time.time()
max = 0
pMax = 0
for i in range(0,len(PRIMES)):
    p = 0
    for j in range(i,len(PRIMES)):
        p += PRIMES[j]
        if UPPER <= p:
            break
        elif p in PRIME_SET and max < j - i + 1:
            max = j - i + 1
            pMax = p
    
print(pMax,'is the sum of',max,'primes')
print("{:.3f}".format(time.time() - startTime))
