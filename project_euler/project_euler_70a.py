#!/usr/bin/python

import time
from euler import readPrimes

def ascending( s ):
    ss = list( s )
    ss.sort()
    return ''.join( ss )

assert( ascending( '56623104' ) == '01234566')

def addPrime( prime, n2totient0, upper, primeMin, nPerm ):
    n2totient = dict( {} )
    for n0 in n2totient0.keys():
        n = n0 * prime
        totient = n2totient0[ n0 ] * (prime - 1)
        while n < upper:
            n2totient[ n ] = totient
            if ascending( str( n ) ) == ascending( str ( totient ) ):
                p = n / (n - totient)
                if primeMin < p:
                    primeMin = p
                    nPerm = n
            n *= prime
            totient *= prime
    n2totient0.update( n2totient )
    return n2totient0, upper, primeMin, nPerm 

PRIME_MIN = 1000.0
primeMin = PRIME_MIN

UPPER = 10**7 # UPPER = 10 # UPPER = 10**5 # 
PRIMES = readPrimes( UPPER / int( primeMin ) )
PRIMES.reverse()

n2totient0 = dict( {1:1} ) # totientRatio = phi(n) / n
nPerm = 0

start = time.time()

i = 0
while i < len( PRIMES ) and primeMin <= PRIMES[ i ]: 
    n2totient0, upper, primeMin, nPerm = addPrime( PRIMES[ i ], n2totient0, UPPER, primeMin, nPerm )
    i += 1

end = time.time()

print(end - start)

assert( nPerm == 8319823 and PRIME_MIN < nPerm / (nPerm - n2totient0[ nPerm ]) )
