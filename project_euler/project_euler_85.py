#!/usr/bin/python

import math

def ascendingFactorialTwos( bound ):
    ascendingFactorialTwos = []
    i = 0
    aft = i * (i + 1)
    while aft < bound:
        ascendingFactorialTwos.append( aft )
        i += 1
        aft = i * (i + 1)
    return ascendingFactorialTwos

BOUND = 8 * 10**6
afts = ascendingFactorialTwos( BOUND )       

i0 = -1
j0 = -1
d0 = math.inf

for i in range( 0, len( afts ) ):
    for j in range( i, len( afts ) ):
        product = afts[ i ] * afts[ j ]
        d = BOUND - product
        if abs( d ) < d0:
            d0 = abs( d )
            i0 = i
            j0 = j
        if d < 0:
            break
            
print( i0, j0, i0 * j0, afts[ i0 ] * afts[ j0 ] )