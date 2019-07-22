#!/usr/bin/python

from euler import isPrime, appendToPrimes

PRIMES = []
UPPER = 10**5
appendToPrimes(UPPER, PRIMES)

twoSquares = [2 * n * n for n in range(0, UPPER)]

n = 3
while True:
    while isPrime(n, PRIMES):
        n += 2
    bad = True
    for j in twoSquares:
        if n <= j:
            break
        if isPrime(n - j, PRIMES):
            bad = False
            n += 2
            break      
    if bad:
        break

print(n)
