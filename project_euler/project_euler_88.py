#!/usr/bin/python

from functools import reduce
from itertools import combinations_with_replacement
from operator import add, mul
from math import log2

def kAndN( ais ):
    n = reduce( mul, ais )
    k = n - reduce( add, ais ) + len( ais )
    return ( k, n )

assert( kAndN( [2,2,2] ) == ( 5, 8 ) )
assert( kAndN( [2,6] ) == ( 6, 12 ) )
assert( kAndN( [2,8] ) == ( 8, 16 ) )
assert( kAndN( [4,4] ) == ( 10, 16 ) )

def k2product( upper ):
    k2product = dict({})
    ns = range( 2, 10 )
    j = 2
    while j <= int( log2( upper ) + 2 ):
        cs = list( combinations_with_replacement( ns, j ) )
        for ais in cs:
            k, n = kAndN( ais )
            if upper < k:
                continue
            if k not in k2product.keys() or n < k2product[ k ][ 0 ]:
                k2product[ k ] = ( n, ais )
        j += 1
    return k2product

d = k2product( 6 )
#assert( sum( list( set( list( d.values() ) ) ) ) == 30 )

d = k2product( 12 )
#assert( sum( list( set( list( d.values() ) ) ) ) == 61 )

d = k2product( 64 )
for k in sorted( d.keys() ):
    print( k, d[ k ] )
    
print( kAndN( [ 2, 24 ] ) )

"""
d = k2product( 24 )
print( sum( list( set( list( d.values() ) ) ) ) )
if upper < k:
                indexes = [ ais[ i ] == ais0[ i ] for i in len( 0, j ) ] 
                for i in range( 0, j ):
                    if not indexes[ i ]:
                        break"""                
    
#print( list( set( list( d.keys() ) ) ) )
#print( list( set( list( d.values() ) ) ) )
#assert( sum( list( set( list( d.values() ) ) ) ) == 61 )

#print( sum( list( set( vs ) ) ) )
#assert( sum( list( set( d.values() ) ) ) == 30 )

#d = k2product( 12 )
#assert( sum( list( set( d.values() ) ) ) == 61 )
