#!/usr/bin/python

import collections

N = 10000

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

# Returns a list of ascending prime factors of n.
def factors(primes, n):

    factors = []
    for p in primes:
        if n == 1:
            return factors
        else:
            while n % p == 0:
                factors.append(p)
                n //= p

    return factors

# Returns the sum of proper factors of n.
def sumProperFactors(n):

    f = factors(primes, n)
#    print(f)
    counter = collections.Counter(f)
#    print(counter)
    sum = 1
    for key in counter:
        sum *= (key ** (counter[key] + 1) - 1) // (key - 1)
    sum -= n
#    print(sum)

    return sum

primes = [2]
extendPrimes(primes, N) # list of primes less than N
#print(primes)

amicable = []
sumFactors = {};
n = 1
while n < N:
    n += 1
    if n not in sumFactors:
        sumFactors[n] = sumProperFactors(n)
        if sumFactors[n] not in sumFactors:
            sumFactors[sumFactors[n]] = sumProperFactors(sumFactors[n])
        if sumFactors[sumFactors[n]] == n and sumFactors[n] != n:
            amicable.append(n)
            amicable.append(sumFactors[n])

amicable.sort()
#print(amicable)

sum = 0
for a in amicable:
    if a >= N:
        break
    else:
        sum += a

print(sum)
