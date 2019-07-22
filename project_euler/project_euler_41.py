#!/usr/bin/python


from itertools import permutations 
from euler import appendToPrimes
from euler import isPrime

BASE = 10
D = 4 # 2143 is a pandigital prime

PRIMES = []
appendToPrimes(10**5, PRIMES)

maximum = 0
for n in range(D,BASE):
    for p in list(permutations(range(1,n+1))):
        i = int(''.join(map(str, p)))
        if isPrime(i, PRIMES):
            if maximum < i:
                maximum = i

print(maximum)