#!/usr/bin/python

FIVE_HUNDRED = 500 # magic constant for # of factors

# Returns true if none of the "primes" divides n.
def isPrime(primes, n):

    for p in primes:
        if p * p > n:
            return True
        elif n % p == 0:
            return False

    return True

# Extends the list of primes up to at least n.
def extendPrimes(primes, n):

    p = primes[-1]

    while p < n:
        p += 1
        if isPrime(primes, p):
            primes.append(p)

    return

# Returns true if none of the "primes" divides n.
def factors(primes, n):

    factors = []
    for p in primes:
        if n == 1:
            return factors
        else:
            while n % p == 0:
                factors.append(p)
                n /= p

    return factors

# Returns the factor count of the product of the primes in the list.
def factorCount(list):

    factorCount = 1

    if len(list) > 0:
        i = 0
        while i < len(list): # i is a new prime
            multiplicity = 1
            i += 1
            while i < len(list) and list[i] == list[i - 1]:
                multiplicity += 1
                i += 1
            factorCount *= multiplicity + 1

    return factorCount

n = 1 # index of triangular number
primes = [2]

while True:
    if n % 2 == 0:
        i = n / 2
        j = n + 1
    else:
        i = (n + 1) / 2
        j = n

    p = primes[-1] # present prime

    while p <= max(i, j):
        p += 1
        if isPrime(primes, p):
            primes.append(p)

    fI = factors(primes, i)
    fJ = factors(primes, j)

    f = sorted(fI + fJ)

    count = factorCount(f)
    if count > FIVE_HUNDRED:
        break

    n += 1

print(n * (n + 1) // 2)

# extendPrimes(primes, 20)
# print(primes)

# print(factors(primes, 18))
# print(factorCount(factors(primes, 18)))