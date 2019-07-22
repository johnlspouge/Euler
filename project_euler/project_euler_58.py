#!/usr/bin/python

from euler import readPrimes
from euler import isPrime

UPPER = 100

def appendDiagonal( ns ):
    delta = ns[ -1 ] - ns[ -2 ]
    delta += 8
    ns.append( ns[ -1 ] + delta )

PRIMES = readPrimes() # complete set of primes up to MAX_PRIME_DIGITCOUNT digits
MAX_PRIME = max( PRIMES )
assert( MAX_PRIME == 15485863 )
PRIME_SET = set( PRIMES )
MAX_TEST = MAX_PRIME * MAX_PRIME

def isTestedPrime( n ):
    if n <= MAX_PRIME:
        return n in PRIME_SET
    elif n <= MAX_TEST:
        return isPrime( n, PRIMES )
    else:
        raise Exception( 'n is too large to test.' )
        
diagonals = [ [ 3, 13, 31 ], [ 5, 17, 37 ], [ 7, 21, 43 ] ]

numerator = 8 
denominator = 13 
ratio = numerator / denominator
    
def appendDiagonals( diagonals ):
    appendDiagonal( diagonals[ 0 ] )
    appendDiagonal( diagonals[ 1 ] )
    appendDiagonal( diagonals[ 2 ] )

appendDiagonals( diagonals )
numerator += sum( [ 1 for i in range( 0, 3 ) if isTestedPrime( diagonals[ i ][ -1 ] ) ] )
denominator += 4
ratio = numerator / denominator
assert( diagonals[ 0 ][ 3 ]  ==  57 )
assert( diagonals[ 1 ][ 3 ]  ==  65 )
assert( diagonals[ 2 ][ 3 ]  ==  73 )
assert( numerator  ==  9 )
assert( denominator  ==  17 )
assert( ratio  ==  9 / 17 )
assert( diagonals[ 1 ][ -1 ] - diagonals[ 0 ][ -1 ] + 1 == 9)

while 0.1 <= ratio:
    appendDiagonals( diagonals )
    numerator += sum( [ 1 for i in range( 0, 3 ) if isTestedPrime( diagonals[ i ][ -1 ] ) ] )
    denominator += 4
    ratio = numerator / denominator

print( diagonals[ 1 ][ -1 ] - diagonals[ 0 ][ -1 ] + 1 )