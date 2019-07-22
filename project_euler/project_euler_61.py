#!/usr/bin/python

from polygonal_numbers import polygonalInverse
from polygonal_numbers import polygonal

LOWER = 10**3
UPPER = 10**4

polygonals = {}

for side in range( 3, 9 ):
    polygonalSides = []
    i = polygonalInverse[ side ]( LOWER )
    polygonalSide = polygonal[ side ]( i )
    while polygonalSide < LOWER:
        i += 1
        polygonalSide = polygonal[ side ]( i )
    while polygonalSide < UPPER:
        polygonalSides.append( polygonalSide )
        i += 1
        polygonalSide = polygonal[ side ]( i )
    polygonals[ side ] = polygonalSides

#print( polygonals )

SIDEA = set( range( 3, 8 ) )
cycle2sidea = dict()
for cycle in polygonals[ 8 ]: # Starts with the smallest set.
    cycle2sidea[ tuple( [ cycle ] ) ] = SIDEA

for n in range( 3, 8 ):
    cycle2sidea0 = cycle2sidea
    cycle2sidea = dict()
    for cycle0 in cycle2sidea0.keys():
        digit2 = cycle0[ -1 ] % 100
        sidea0 = cycle2sidea0[ cycle0 ]
        for side in list( sidea0 ):
            sidea = sidea0.difference( set( [ side ] ) )
            ns = [ n for n in polygonals[ side ] if n // 100 == digit2 ]
            for n in ns:
                cycle = cycle0 + tuple( [ n ] )
                cycle2sidea[ cycle ] = sidea

assert( all( len( sidea ) == 0 for sidea in cycle2sidea.values() ) )

paths = cycle2sidea.keys()
cycles = [ path for path in paths if path[ 0 ] // 100 == path[ -1 ] % 100 ]
assert( len( cycles ) == 1 )
print( cycles[ 0 ] )
print( sum( cycles[ 0 ] ) )