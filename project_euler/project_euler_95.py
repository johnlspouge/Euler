#!/usr/bin/python

from math import sqrt
from euler import appendToPrimes
from euler import primeFactors
from euler import primePowerFactorization
from euler import isPrime

N = 1000001 # N = 16000 # 

primes = []
appendToPrimes(int(sqrt(N) + 1), primes)

def sumFactors(n):
    if isPrime(n, primes):
        return 1
    ps = primeFactors(n, primes)
    pPowers = primePowerFactorization(ps)
    sum = 1
    for p in pPowers.keys():
        sum *= (p ** (pPowers[p] + 1) - 1) // (p - 1)
    return sum - n

assert(sumFactors(6) == 6)
assert(sumFactors(28) == 28)
assert(sumFactors(220) == 284)
assert(sumFactors(284) == 220)
assert(sumFactors(12496) == 14288)
assert(sumFactors(14288) == 15472)
assert(sumFactors(15472) == 14536)
assert(sumFactors(14536) == 14264)
assert(sumFactors(14264) == 12496)
assert(sumFactors(180) == 366)

# 12496 → 14288 → 15472 → 14536 → 14264 → 12496
"""
n = 12496
m = n
cycle = []
while m != n or len(cycle) == 0:
    cycle.append(m)
    m = sumFactors(m)

print(cycle)
"""
longest = 0
cycle = []
checked = set()
checked.add(1)

#for n in range(2,N):
for n in range(2,N):
    if n in checked:
        continue
    iterates = []
    m = n
    while m not in checked and m < N:
        checked.add(m)
        iterates.append(m)
        m = sumFactors(m)
    if N <= m:
        continue
    if m in iterates:
        while iterates[0] != m:
            iterates.pop(0)
        if longest < len(iterates):
            minimum = min(iterates)
            longest = len(iterates)
            cycle = iterates

print(cycle)
print(minimum)
