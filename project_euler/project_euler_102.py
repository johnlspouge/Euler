#!/usr/bin/python

from numpy.linalg import det
from copy import deepcopy

def sign( x ):
    if x > 0:
        return +1
    elif x < 0:
        return -1
    return 0

def signSide( pts_, pt_ ):
    pts = deepcopy( pts_ )
    pt = deepcopy( pt_ )
    pts[ 0 ].append( 1 )
    pts[ 1 ].append( 1 )
    pt.append( 1 )
    matrix = [ pts[ 0 ], pts[ 1 ], pt ]
    return sign( det( matrix ) )

pts_ = [ [ 0, 1 ], [ 1, 0 ] ]
pt_ = [ 1, 1 ]
sign_ = signSide( pts_, pt_ )
pt0 = [ 2, 2 ]
sign0 = signSide( pts_, pt0 )
assert( sign0 == sign_ )

def sameSide( pts, pt0, pt1 ):
    return signSide( pts, pt0 ) == signSide( pts, pt1 )

def inside( pts, pt ):
    s0 = sameSide( [ pts[ 1 ], pts[ 2 ] ], pts[ 0 ], pt )
    s1 = sameSide( [ pts[ 0 ], pts[ 2 ] ], pts[ 1 ], pt )
    s2 = sameSide( [ pts[ 0 ], pts[ 1 ] ], pts[ 2 ], pt )
    return s0 and s1 and s2

count = 0
pt = [ 0, 0 ]
with open( 'Data/p102_triangles.txt', 'r' ) as myfile:
    line = myfile.readline()
    while line:
        coords = line.split( ',' )
        pts = []
        pts.append( [ int( coords[ 0 ] ), int( coords[ 1 ] ) ] )
        pts.append( [ int( coords[ 2 ] ), int( coords[ 3 ] ) ] )
        pts.append( [ int( coords[ 4 ] ), int( coords[ 5 ] ) ] )
        if inside( pts, pt ):
            count += 1
        line = myfile.readline()

assert( count == 228 )
