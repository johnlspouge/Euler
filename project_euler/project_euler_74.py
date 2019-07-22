#!/usr/bin/python

# Returns squares[0...upper].
def squares( upper ):
    squares = []
    for n in range( 0, upper + 1 ):
        squares.append( n * n )
    return squares

UPPER = 9
SQUARES = squares( UPPER )

assert( SQUARES[ 0 ] == 0 )
assert( SQUARES[ 3 ] == 9 )
assert( SQUARES[ 5 ] == 25 )

def sumSquareDigits( n ):
    digits = list( str( n ) )
    return sum( [ SQUARES[ int( digit ) ] for digit in digits ] )

assert( sumSquareDigits( 44 ) == 32 )
assert( sumSquareDigits( 32 ) == 13 )
assert( sumSquareDigits( 85 ) == 89 )
assert( sumSquareDigits( 89 ) == 145 )

def ascending( n ):
    digits = list( str( n ) ) 
    digits.sort()
    return int( ''.join( digits ) )

assert( ascending( 3968 ) == 3689 )
assert( ascending( 32 ) == 23 )

n2chainEnd = dict({1:1,89:89})
end = set( { 1, 89 } )

def chainEnd( n ):
    ns = []
    n = ascending( n ) 
    while n not in n2chainEnd.keys():
        ns.append( n )
        n = ascending( sumSquareDigits( n ) )
    chainEnd = n2chainEnd[ n ]
    for m in ns:
        n2chainEnd[ m ] = chainEnd
    return chainEnd
        
assert( chainEnd( 44 ) == 1 )
assert( n2chainEnd[ 23 ] == 1 )
assert( n2chainEnd[ 1 ] == 1 )
assert( chainEnd( 85 ) == 89 )
assert( 145 not in n2chainEnd.keys() )
assert( chainEnd( 145 ) == 89 )
assert( n2chainEnd[ 24 ] == 89 )
assert( chainEnd( 16 ) == 89 )
assert( n2chainEnd[ 16 ] == 89 )

LIMIT = 10**7

print( sum( [ 1 for n in range( 1, LIMIT ) if chainEnd( n ) == 89 ] ) )# == 402 )