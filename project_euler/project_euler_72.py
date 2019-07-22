#!/usr/bin/python

from euler import readPrimes
from bisect import insort
import time

UPPER = 10**6 # UPPER = 8 # 
PRIMES = readPrimes( UPPER )

# Constructs table of non-0 mobius function values.
# Time-complexity is O( P * A * (log A)**2 ) 
#   P = #{ primes <= upper }, A = #{ stored Mobius arguments }
def n2mobius( upper, primes ):
    n2mobius = dict({1:1})
    keys = [ 1 ]
    for p in primes:
        if upper < p:
            break
        keys0 = []
        for n in keys:
            if upper < p * n:
                break
            n2mobius[ p * n ] = -n2mobius[ n ]
            keys0.append( p * n )
        for key0 in keys0:
            insort( keys, key0 )
    return n2mobius

def mobiusFctAll( n, mobiusFct ):
    if n in mobiusFct.keys():
        return mobiusFct[ n ]
    return 0

mobiusFct = n2mobius( 20, PRIMES )
assert( mobiusFctAll( 1, mobiusFct ) == 1 )
assert( mobiusFctAll( 2, mobiusFct ) == -1 )
assert( mobiusFctAll( 4, mobiusFct ) == 0 )
assert( mobiusFctAll( 6, mobiusFct ) == 1 )
assert( mobiusFctAll( 8, mobiusFct ) == 0 )
assert( mobiusFctAll( 10, mobiusFct ) == 1 )

def F( n ):
    return n * (n - 1) // 2

assert( F( 8 ) == 28 )

def fareyLength( n, mobiusFct ):
    length = 0
    for m in range( 1, n + 1 ):
        mobiusFctM = mobiusFctAll( m, mobiusFct )
        if mobiusFctM == 0:
            continue
        length += mobiusFctM * F( n // m )
    return length

upper = 10
mobiusFct = n2mobius( upper, PRIMES )
assert( fareyLength( 8, mobiusFct ) == 21  )
assert( fareyLength( 9, mobiusFct ) == 27  )

upper = 10**6
start = time.time()
mobiusFct = n2mobius( upper, PRIMES )
print( time.time() - start ) # 28.9 secs
start = time.time()
assert( fareyLength( upper, mobiusFct ) == 303963552391 )
print( time.time() - start ) # 0.344 secs
