#!/usr/bin/python

from collections import Counter
from itertools import permutations

def isCube( n ):
    EPS = 1.0e-10
    m = int( (1.0 + EPS) * (n ** (1/3)) )
    return m * m * m == n

assert( isCube( 345**3 ))
assert( isCube( 384**3 ))
assert( isCube( 405**3 ))
assert( isCube( 41063625 ))
assert( isCube( 56623104 ))
assert( isCube( 66430125 ))

def countPermutationsThatAreCube( n ):
    perms = set( map( ''.join, permutations ( str( n ) ) ) )
    return sum( [ 1 for p in list( perms ) if isCube( int( str( p ) ) ) and p[0] != '0' ] )

assert( countPermutationsThatAreCube( 345**3 ) == 3 )

def smallestCubeWithCount( count ):   
    n = 1
    while countPermutationsThatAreCube( n * n * n ) != count:
        n += 1
    return n * n * n

assert( smallestCubeWithCount( 3 ) == 41063625 )

# The above takes too long for 
#print( smallestCubeWithCount( 5 ))

def cube( n ):
    return n * n * n

def ascending( s ):
    ss = list( s )
    ss.sort()
    return ''.join( ss )

assert( ascending( '56623104' ) == '01234566')

def cubeWithCount( count ):
    cubeWithCounts = []
    digitCount = 0
    i = 1
    n = cube( i )
    while True:
        digitCount += 1
        N = 10**digitCount
        cubes = []
        while n < N: # Accumulates cubes with count digits in cubes.
            cubes.append( str( n ) )
            i += 1
            n = cube( i )
        ascendings = [ ascending( s ) for s in cubes ]
        c = Counter( ascendings )
        ascendingWithCounts = [ a for a,v in c.items() if v == count ]
        for ascendingWithCount in ascendingWithCounts:
            cs = [ s for s in cubes if ascending( s ) == ascendingWithCount ]
            cubeWithCounts.append( cs[ 0 ] )
        if len( cubeWithCounts ) != 0:
            cubeWithCounts.sort()
            return int( cubeWithCounts[ 0 ] )

assert( cubeWithCount( 3 ) == 41063625 )
CUBE_WITH_COUNT_5 = 127035954683
assert( cubeWithCount( 5 ) == CUBE_WITH_COUNT_5)
print( CUBE_WITH_COUNT_5 )