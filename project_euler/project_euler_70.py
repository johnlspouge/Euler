#!/usr/bin/python

from euler import readPrimes, primeFactors, primePowerFactorization
import math

UPPER = 10**7
LIMIT = UPPER
PRIMES = readPrimes( LIMIT )

def totient( n, primes ):
    pFs = primeFactors( n, primes )
    ppFm = primePowerFactorization( pFs )
    ppFmKeys = ppFm.keys()
    totient = n
    for primeFactor in ppFmKeys:
        totient = totient - totient / primeFactor
    return totient

assert( totient( 1, PRIMES ) == 1 )
assert( totient( 9, PRIMES ) == 6 )
assert( totient( 87109, PRIMES ) == 79180 )

def ascending( s ):
    ss = list( s )
    ss.sort()
    return ''.join( ss )

assert( ascending( '56623104' ) == '01234566')

minimum = math.inf

out = 10**5

for n in range( 2, UPPER ):
    if n % out == 0:
        print( n )
    t = totient( n, PRIMES )
    if ascending( str( t ) ) != ascending( str( n ) ):
        continue
    if n / t < minimum:
        minimum = n / t
        nMinimum = n

print( nMinimum )