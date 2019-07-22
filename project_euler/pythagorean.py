#!/usr/bin/python

# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

from copy import deepcopy 

def isPythagorean( ps ):
    a = ps[ 0 ]
    b = ps[ 1 ]
    c = ps[ 2 ]
    return c * c == a * a + b * b

# Produces children in the ternary tree.
    # Every child has a longer hypotenuse.
def _childPs( ps ):
    a = ps[ 0 ]
    b = ps[ 1 ]
    c = ps[ 2 ]
    childPs = []
    childPs.append( (  a - 2 * b + 2 * c,  2 * a - b + 2 * c,  2 * a - 2 * b + 3 * c ) )
    childPs.append( (  a + 2 * b + 2 * c,  2 * a + b + 2 * c,  2 * a + 2 * b + 3 * c ) )
    childPs.append( ( -a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c ) )
    return childPs

assert( _childPs( ( 3, 4, 5 ) ) == [ (5, 12, 13), (21, 20, 29), (15, 8, 17) ] )

# Reorders triples, so that a <= b <= c.
def _toIncreasingTriple( ps ):
    a, b, c = ps
    a, b = min( a, b ), max( a, b )
    return a, b, c

# Returns set of all the primitive Pythagorean triples (in order a <= b <= c)
#   satisfying condition( primitive ) = True.
# Assumes that condition( primitive ) = False => condition( children ) = False.
#   In particular, if the condition fails for a larger hypotenuse, the algorithm is correct.
def primitiveIncreasingPythagoreanTripleA( condition ):
    queue = [ ( 3, 4, 5 ) ]
    primitives = [] 
    while len( queue ) != 0:
        primitive = queue.pop( 0 )
        if condition( primitive ):
            primitives.append( _toIncreasingTriple( primitive ) )
            queue.extend( _childPs( primitive ) )
    assert( len( queue ) == 0 )
    return set( primitives )

c = 50
def isHypotenuseLessThan( pythagorean ):
    return pythagorean[ 2 ] < c

primitiveA = primitiveIncreasingPythagoreanTripleA( isHypotenuseLessThan )
assert( 
       
    sorted( list( primitiveA ) ) == [ 
            
        ( 3,  4,  5), ( 5, 12, 13), ( 7, 24, 25), ( 8, 15, 17), ( 9, 40, 41), 
        (12, 35, 37), (20, 21, 29) 
    ] 
)

# Returns all the primitive Pythagorean triples (in order a <= b <= c)
#   satisfying condition( primitive ) = True.
def allIncreasingPythagoreanTripleA( condition ):
    primitiveA = primitiveIncreasingPythagoreanTripleA( condition )
    gcd = 2
    pythagoreanA = deepcopy( primitiveA )
    smallPrimitiveA = deepcopy( primitiveA )
    while len( smallPrimitiveA ) != 0:
        smallPrimitiveA = { primitive for primitive in smallPrimitiveA if condition( [ gcd * p for p in primitive ] ) }
        pythagoreanA = pythagoreanA.union( { tuple( [ gcd * p for p in primitive ] ) for primitive in smallPrimitiveA } )
        gcd += 1
    assert( all( [ isPythagorean( pythagorean ) for pythagorean in pythagoreanA ] ) )
    assert( all( [ condition( pythagorean ) for pythagorean in pythagoreanA ] ) )
    return pythagoreanA

pythagoreanA = allIncreasingPythagoreanTripleA( isHypotenuseLessThan )
assert( 
       
    sorted( list( pythagoreanA ) ) == [ 
            
        ( 3,  4,  5), ( 5, 12, 13), ( 6,  8, 10), ( 7, 24, 25), ( 8, 15, 17), 
        ( 9, 12, 15), ( 9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), 
        (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), 
        (21, 28, 35), (24, 32, 40), (27, 36, 45)
    ] 
)
