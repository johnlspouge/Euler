#!/usr/bin/python

from math import log
from math import sqrt
from euler import appendToPrimes
from euler import isPrime
from euler import appendDigitsUnsorted

N = 1000000 # N = 100 # 
BASE = 10

primes = []
appendToPrimes(int(sqrt(N)), primes)
# print(primes) # [2, 3, 5, 7]

a = int(sqrt(N))
while a < N:
    if isPrime(a, primes):
        primes.append(a)
    a += 1

# primes contains all primes less than N.
# print(primes) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

possibles = [] # potentially right truncatable: no internal {0,2,4,5,6,8} and no left {0,4,6,8}
for p in primes:
    digits = appendDigitsUnsorted(p, [])
    if 0 in digits or 4 in digits or 6 in digits or 8 in digits:    
        continue
    digits.pop(0)
    if 2 in digits or 5 in digits:    
        continue
    possibles.append(p)
# print(possibles) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 53, 59, 71, 73, 79, 97]

rights = []
for p in possibles:
    isTruncatable = True
    p0 = p
    while p0 >= BASE:
        p0 //= BASE # Deletes the right-most digit
        if p0 not in primes:
            isTruncatable = False
            break
    if isTruncatable:
        rights.append(p)

# print(right) # [2, 3, 5, 7, 23, 29, 31, 37, 53, 59, 71, 73, 79]

lefts = [] # left truncatable
for p in rights:
    isTruncatable = True
    p0 = p
    while p0 >= BASE:
        p0 %= BASE ** int(log(p0, BASE)) # Deletes the left-most digit
        if p0 not in primes:
            isTruncatable = False
            break
    if isTruncatable:
        lefts.append(p)
# print(lefts) # [2, 3, 5, 7, 23, 37, 53, 73]
# [2, 3, 5, 7, 37, 73, 313, 317, 373, 797, 3137, 3797, 739397]

lefts = [value for value in lefts if value > BASE]
print(lefts) 
print(len(lefts))
print(sum(lefts))