#!/usr/bin/python

ITERATION = 49
UPPER = 10**4

def reverseToNumber( n ):
    digits = list( str( n ) )
    digits.reverse()
    return int( ''.join( digits ) )

assert( reverseToNumber( 490 ) == 94 )

def isPalindrome( n ):
    return reverseToNumber( n ) == n

assert( isPalindrome( 7337 ) )
assert( isPalindrome( 121 ) )
assert( isPalindrome( 4668731596684224866951378664 ) )

def lychrelize( n ):
    return n + reverseToNumber( n )

assert( lychrelize( 74 ) == 121 ) 
assert( lychrelize( 349 ) == 1292 )

def isLychrel( n, reps = ITERATION ):
    m = n
    for i in range( 0, reps ):
        m = lychrelize( m )
        if isPalindrome( m ):
            return False
    return True

assert( isLychrel( 196 ) )
assert( isLychrel( 10677 ) )
assert( not isLychrel( 10677, 53 ) )

print( sum( [ 1 for n in range( 1, UPPER ) if isLychrel( n )  ] ) )