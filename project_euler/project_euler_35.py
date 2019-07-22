#!/usr/bin/python

from math import log10
from math import sqrt
from euler import isPrime
from euler import appendToPrimes

N = 1000000 # N = 100 
BASE = 10

primes = []
appendToPrimes(int(sqrt(N)), primes)
# print(primes) # [2, 3, 5, 7]

a = int(sqrt(N))
while a < N:
    if isPrime(a, primes):
        primes.append(a)
    a += 1

# print(primes) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

rotates = []
for p in primes:
    if p in rotates:
        continue
    powerOf10 = 10 ** int(log10(p)) 
    ps = [] # potentially rotating primes
    p0 = p
    while len(ps) == 0 or p0 != p:
        if p0 not in primes:
            ps = []
            break
        else:
            ps.append(p0)
            p0 = (p0 % BASE) * powerOf10 + p0 // BASE # cyclic rotate
    rotates += ps

rotates.sort()
print(rotates) # [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
# [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331]
print(len(rotates)) # 55