#!/usr/bin/python

from collections import Counter
import math
from numpy import prod
import itertools

def gcd( a, b ):
    a0 = max( a, b )
    b0 = min( a, b )
    while b0 != 0:
        a0 %= b0
        a0, b0 = b0, a0
    return a0

def isSquare(n):
    m = int(math.sqrt(n))
    return m * m == n or (m + 1) * (m + 1) == n

def integerSqrt(n):
    m = int(math.sqrt(n))
    if m * m == n:
        return m
    m += 1
    if m * m == n:
        return m
    return -1

def readPrimes( limit = 0 ):
    primes = []
    with open( 'Data/primes2to15485863.txt', 'r' ) as myfile:
        for i in range(0, 4):
            line = myfile.readline()
        while line:
            line = myfile.readline()
            if not line.strip():
                continue
            ps = [ int(s) for s in line.split() if s.isdigit()]
            if limit == 0 or ps[ -1 ] <= limit:
                primes.extend( ps )
            elif limit < ps[ 0 ]:
                break
            else:
                primes.extend( [ p for p in ps if p <= limit ] )
    return primes
    
# primes holds a complete list of primes from 1 to sqrt(n).
# Returns True if none of the primes divides n.
def isPrime(n, primes):

    if len(primes) == 0:
        appendToPrimes(int(math.sqrt(n)), primes)
        
    for p in primes:
        if p * p > n:
            return True
        elif n % p == 0:
            return False

    return True

# Extends (possibly empty) list of primes up to at least n.
# Returns extended list (for default = None)
def appendToPrimes(n, primes):

    if len(primes) == 0:
        primes.append(2)
    p = primes[-1]

    while p < n:
        p += 1
        if isPrime(p, primes):
            primes.append(p)
 
    return primes

# Returns a list of prime factors of n.
def primeFactors(n, primes):

    if len(primes) == 0:
        appendToPrimes(int(math.sqrt(n) + 1), primes)
        
    primeFactors = []
    for p in primes:
        if n == 1:
            return primeFactors
        else:
            while n % p == 0:
                primeFactors.append(p)
                n //= p
    if n != 1:
        primeFactors.append(n)
    return primeFactors

# Returns a map from primes to their powers in primeFactors.
def primePowerFactorization(primeFactors):

    primePowerFactorization = Counter(primeFactors)
    
    return primePowerFactorization

def totient( n, primes ):
    pFs = primeFactors( n, primes )
    ppFm = primePowerFactorization( pFs )
    ppFmKeys = ppFm.keys()
    totient = n
    for primeFactor in ppFmKeys:
        totient = totient - totient // primeFactor
    return totient

def ascendingFactorial(n, k):
    
    if k < 0:
        return 1 / descendingFactorial(n - 1, -k)
    
    product = 1
    j = 0
    while j < k:
        product *= n + j
        j += 1
    
    return product

def descendingFactorial(n, k):
    
    if k < 0:
        return 1 / ascendingFactorial(n + 1, -k)
    
    product = 1
    j = 0
    while j < k:
        product *= n - j
        j += 1
    
    return product

def appendDigits(n, d, base = 10):
    while n > 0:
        d.append(n % base)
        n //= base
    d.sort()
    return d

def appendDigitsUnsorted(n, d, base = 10):
    while n > 0:
        d.append(n % base)
        n //= base
    d.reverse()
    return d

def factors(n, primes):
    ps = primeFactors(n, primes)
    fsets = []
    m = 1
    while m <= len(ps):
        fsets += list(itertools.combinations(ps,m))
        m += 1
    fsets = list(set(fsets))
    products = list(map(prod, fsets))
    products.insert(0,1)
    products.sort()
    return products
