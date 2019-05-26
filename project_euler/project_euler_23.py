#!/usr/bin/python

import collections

N = 28124

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
def sumProperDivisors(n):

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

abundant = []
sumFactors = {};
n = 1
while n < N:
    if sumProperDivisors(n) > n:
        abundant.append(n)
    n += 1

#print(abundant)

sumTwoAbundants = []

i = 0
while i < len(abundant):
    j = 0
    while j <= i:
        sumTwoAbundants.append(abundant[i] + abundant[j])
        j += 1
    i += 1

dict = {}
for a in sumTwoAbundants:
    dict[a] = 0

#print(dict)
list = list(dict.keys())
#print(list)

i = 0
sum = 0
n = 1
while n < N:
    if n == list[i]:
        i += 1
    else:
        sum += n
    n += 1

print(sum)
