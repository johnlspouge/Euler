#!/usr/bin/python

from euler import isPrime
from euler import readPrimes

#PRIME_LIMIT = 10**6
#PRIMES = readPrimes( PRIME_LIMIT ) # list of primes up to PRIME_LIMIT
PRIMES = readPrimes() # list of 1st million primes
PRIMECS = list( map( str, PRIMES ) ) # list PRIMES as strings
PRIMECA = set( PRIMECS ) # set of PRIMECS 

assert( PRIMECS[ 0 ] == '2' )

def isPrimeString( s ):
    if s in PRIMECA:
        return True
    n = int( s )
    if PRIMES[ -1 ] * PRIMES[ -1 ] < n:
        raise Exception( 'isPrimeString: PRIMES[ -1 ] * PRIMES[ -1 ] < n' )
    else:
        return isPrime( n, PRIMES )

def isConcatenable( p0, p1 ):
    return isPrimeString( p0 + p1 ) and isPrimeString( p1 + p0 )

assert( isConcatenable( '3', '7' ) )
assert( isConcatenable( '109', '673' ) )
assert( not isConcatenable( '2', '37' ) )

def concatenableTuple( SIZE ):
# Returns the first set with size size of concatenable PRIMECS not exceeding maximum.
# Returns None if none exists.
    hyperEdges = {} # list of concatenable tuples of PRIMECS
    hyperEdges[ 2 ] = [] # list of concatenable pairs of PRIMECS

    for i in range( 0, len( PRIMECS ) ): # largest of a pair of concatenable PRIMECS
        p0 = PRIMECS[ i ]
        # Converts to integer PRIMECS. Strings are no longer useful.
        vertices = [ PRIMES[ j ] for j in range( 0, i ) if isConcatenable( PRIMECS[ j ], p0 ) ]
        p0 = int( p0 )
        n = max( hyperEdges.keys() )
        while n >= 2:
            for hyperEdge in hyperEdges[ n ]:
                if all( [ p in vertices for p in hyperEdge ] ):
                    hyperEdge0 = hyperEdge + tuple( [ p0 ] ) # (n + 1)-tuple of concatenable PRIMECS
                    if n == SIZE - 1: # found a SIZE tuple of concatenable PRIMECS
                        return hyperEdge0 # smallest SIZE tuple
                    elif n + 1 in hyperEdges.keys():
                        hyperEdges[ n + 1 ].append( hyperEdge0 )
                    else:
                        hyperEdges[ n + 1 ] = [ hyperEdge0 ]
            n -= 1
        hyperEdges[ 2 ] += [ ( p, p0 ) for p in vertices ]
    return None

print( PRIMES[ -1 ])

CONCATENABLETUPLE_3 = concatenableTuple( 3 )
print( CONCATENABLETUPLE_3 )
assert( CONCATENABLETUPLE_3 == (3, 37, 67) )

CONCATENABLETUPLE_4 = concatenableTuple( 4 )
print( CONCATENABLETUPLE_4 )
assert( CONCATENABLETUPLE_4 == (3, 7, 109, 673) )

CONCATENABLETUPLE_5 = concatenableTuple( 5 )
print( CONCATENABLETUPLE_5 )
assert( CONCATENABLETUPLE_5 == (13, 5197, 5701, 6733, 8389) )

print( sum( CONCATENABLETUPLE_5 ))
