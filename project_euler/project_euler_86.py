#!/usr/bin/python

# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

import pythagorean

def countOfCuboidsRotationsEquivalent( ps ):
    a, b, c = ps
    count = a // 2 # a is the sum of two cuboid edges
    count += max( 0, a - (b - 1) // 2 ) # b is the sum of two cuboid edges
    return count

assert( countOfCuboidsRotationsEquivalent( ( 3, 4, 5 ) ) == 3 )
# 1, 2, 4 
# 1, 3, 3 
# 2, 2, 3 

M = 100 # 

def condition( triple ):
    return triple[ 2 ] <= 
"""



count = 0
for pythagorean in pythagoreanTriples( M ):
    count += countOfCuboids( pythagorean )        

print( count )
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
"""