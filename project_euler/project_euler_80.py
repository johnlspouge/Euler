#!/usr/bin/python

from mpmath import *
mp.dps = 200

FIRST = 100

def squareRoot( n ): 
    assert( 0 <= n )
    return sqrt( mpf( str( n ) ) )

def sumDigits( x ): 
    digits = list( str( x ) )
    if '.' in digits:
        digits.remove( '.' )
    return sum( [ int( digits[ i ] ) for i in range( 0, FIRST ) ] )

assert( sumDigits( squareRoot( 2 ) ) == 475 )

# Main

total = 0
i = 1
for n in range( 1, 100 ):
    if n == i * i:
        i += 1
        continue
    total += sumDigits( squareRoot( n ) )
        
assert( total == 40886)