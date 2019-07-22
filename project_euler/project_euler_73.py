#!/usr/bin/python

from euler import gcd
import math

UPPER = 12000
 
assert( int( -3.2 ) == -3 )

assert( gcd( 32, 12 ) == 4 )
assert( gcd( 32, 11 ) == 1 )

def countReduced( b, x, y ):
# Counts reduced fractions x < a / b < y
    x0 = min( x, y )
    y0 = max( x, y )
    assert( x0 <= y0 )
    
    count = 0
    for a in range( 1 + int( b * x ), int( math.ceil( b * y ) + 0.5 ) ):
        if gcd( a, b ) == 1:
            count += 1
    return count

assert( countReduced( 8, 1/3, 1/2 ) == 1)
assert( countReduced( 5, 1/3, 1/2 ) == 1)
assert( countReduced( 7, 1/3, 1/2 ) == 1)
assert( countReduced( 4, 1/3, 1/2 ) == 0)

def countTotalReduced( upper, x, y ):
# Counts reduced fractions x < a / b < y for 2 <= b <= upper
    total = 0
    for b in range( 2, upper + 1):
        total += countReduced( b, 1/3, 1/2 )
    return total

assert( countTotalReduced( 8, 1/3, 1/2 ) == 3 )
assert( countTotalReduced( UPPER, 1/3, 1/2 ) == 7295372 )