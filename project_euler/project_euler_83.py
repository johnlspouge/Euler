#!/usr/bin/python

# https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

import math
from itertools import product

def newMatrix( m, n, v ):
    matrix = []
    for i in range( 0, m ):
        matrix.append( [v] * n )
    return matrix

def neighbors( i, m ):
    return [ k for k in range( max( 0, i - 1 ), min( m - 1, i + 1 ) + 1 ) if k != i ]

assert( neighbors( 4, 5 ) == [ 3 ] )
assert( neighbors( 4, 7 ) == [ 3, 5 ] )
assert( neighbors( 0, 7 ) == [ 1 ] )
assert( neighbors( 0, 5 ) == [ 1 ] )
assert( neighbors( 1, 5 ) == [ 0, 2 ] )

def value( i, j, matrix, sumMatrix ):
    m = len( matrix )
    n = len( matrix[ 0 ] )
    ims = neighbors( i, m )
    vs = list( product( ims, [ j ] ) )
    jns = neighbors( j, n )
    vs.extend( list( product( [ i ], jns ) ) )
    value = min( [ sumMatrix[ v[ 0 ] ][ v[ 1 ] ] for v in vs ] )
    value += matrix[ i ][ j ]
    return value

def isChange( matrix, sumMatrix ):
    m = len( matrix )
    n = len( matrix[ 0 ] )
    isChange = True
    while isChange:
        isChange = False
        for i in range( 0, m ):
            for j in range( 0, n ):
                v = value( i, j, matrix, sumMatrix ) 
                if v < sumMatrix[ i ][ j ]:
                    sumMatrix[ i ][ j ] = v
                    isChange = True
    return isChange

def initialize( matrix ):
    m = len( matrix )
    n = len( matrix[ 0 ] )
    sumMatrix = newMatrix( m, n, math.inf )
    sumMatrix[ 0 ][ 0 ] = matrix[ 0 ][ 0 ]
    return sumMatrix

def sumMatrix( matrix ):
    sumMatrix = initialize( matrix )
    while isChange( matrix, sumMatrix ):
        pass
    return sumMatrix

matrix = [
[ 131,673,234,103,18 ],
[ 201,96,342,965,150 ],
[ 630,803,746,422,111 ],
[ 537,699,497,121,956 ],
[ 805,732,524,37,331 ]
]

minPaths = sumMatrix( matrix )
assert( minPaths[ -1 ][ -1 ] == 2297 )

matrix = []
with open( 'Data/p083_matrix.txt', 'r' ) as myfile:
    line = myfile.readline()
    while line:
        matrix.append( [ int( field ) for field in line.split( ',' ) ] )
        line = myfile.readline()

minPaths = sumMatrix( matrix )
assert( minPaths[ -1 ][ -1 ] == 425185 )
