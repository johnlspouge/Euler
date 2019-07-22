#!/usr/bin/python

# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

from copy import deepcopy 

def isPythagorean( ps ):
    a = ps[ 0 ]
    b = ps[ 1 ]
    c = ps[ 2 ]
    return c * c == a * a + b * b

def childPs( ps ):
    a = ps[ 0 ]
    b = ps[ 1 ]
    c = ps[ 2 ]
    childPs = []
    childPs.append( (  a - 2 * b + 2 * c,  2 * a - b + 2 * c,  2 * a - 2 * b + 3 * c ) )
    childPs.append( (  a + 2 * b + 2 * c,  2 * a + b + 2 * c,  2 * a + 2 * b + 3 * c ) )
    childPs.append( ( -a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c ) )
    return childPs

# Perimeter of parent p = a + b + c
# Perimeters of children:
    # 5 * a - 5 * b + 7 * c > p
    # 5 * a + 5 * b + 7 * c > p
    # -5 * a + 5 * b + 7 * c > p
    
assert( childPs( ( 3, 4, 5 ) ) == [ (5, 12, 13), (21, 20, 29), (15, 8, 17) ] )

def add( ps, p2pythagoreana ):
    p = sum( ps ) 
    a, b, c = ps
    a, b = min( a, b ), max( a, b )
    if p in p2pythagoreana.keys():
        p2pythagoreana[ p ].add( ( a, b, c ) )
    else:
        p2pythagoreana[ p ] = set( { ( a, b, c ) } )
    
L = 1500000 # L = 150 # 

queue = [ ( 3, 4, 5 ) ]
primitives = [] 
while len( queue ) != 0:
    primitive = queue.pop( 0 )
    perimeter = sum( primitive )
    if perimeter <= L:
        primitives.append( primitive )
        queue.extend( childPs( primitive ) )
assert( len( queue ) == 0 )

# Now, primitives contains all the primitive Pythagorean triples with perimeters not exceeding L.

gcd = 2
pythagoreans = deepcopy( primitives )
smallPrimitives = deepcopy( primitives )
while len( smallPrimitives ) != 0:
    smallPrimitives = [ primitive for primitive in smallPrimitives if sum( [ gcd * p for p in primitive ] ) <= L ]
    pythagoreans.extend( [ tuple( [ gcd * p for p in primitive ] ) for primitive in smallPrimitives ] ) 
    gcd += 1

assert( all( [ isPythagorean( pythagorean ) for pythagorean in pythagoreans ] ) )
assert( all( [ sum( pythagorean ) <= L for pythagorean in pythagoreans ] ) )

# Now, pythagoreans contains all the Pythagorean triples with perimeters not exceeding L.

p2pythagoreana = dict({})
for pythagorean in pythagoreans:
    add( pythagorean, p2pythagoreana )    
     
assert( min( p2pythagoreana.keys() ) == 12 )
assert( len( p2pythagoreana[ 12 ] ) == 1 )        
assert( 20 not in p2pythagoreana.keys() )    
assert( p2pythagoreana[ 120 ] == {(24, 45, 51), (20, 48, 52), (30, 40, 50)} )     
assert( len( p2pythagoreana[ 120 ] ) == 3 )        

count = sum( [ 1 for p in p2pythagoreana.keys() if len( p2pythagoreana[ p ] ) == 1 ] )            
assert( count == 161667 )
