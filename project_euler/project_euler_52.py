#!/usr/bin/python

import itertools 
import math

BASE = 10
MS = range( 2, 7 )

# Sorts the digits of nstr in ascending order.
def canonical( nstr ):
    ns = list( nstr )
    ns.sort() 
    return ''.join( ns )

# Returns a success; otherwise 0.
def success( length ):
    ns = list( range(BASE ** (length - 1), BASE ** length ) )
    for n in ns:
        nstr = canonical( str( n ) )
        if all( [ canonical( str( m * n ) ) == nstr for m in MS ]):
            return n
    return 0


length = 1
while True:
    n = success( length )
    if n != 0:
        break;
    length += 1

print( n )        