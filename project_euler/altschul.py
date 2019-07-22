#!/usr/bin/python

from euler import readPrimes, primeFactors, primePowerFactorization
from operator import mul
from functools import reduce

UPPER = 1000 

primes = readPrimes( UPPER )

d0 = 1

for n in range( 2, UPPER ):
    pfs = primeFactors(n, primes)
    p2power = primePowerFactorization(pfs)
    values = list( p2power.values() )
    if len( values ) == 1:
        sigma0 = 1 + values[ 0 ]
    else:       
        sigma0 = reduce( mul, [ (1 + value ) for value in values ] )
    if d0 < sigma0:
        d0 = sigma0
        print( n )
