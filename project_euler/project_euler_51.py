#!/usr/bin/python

import itertools 
import math
from euler import appendDigitsUnsorted, appendToPrimes, readPrimes

BASE = 10
INDEXES = range( 0, BASE )

# Does the list of digits match in the positions indexed by c?
def isMatch( digits, c ):
    digit0 = digits[ c[ 0 ] ]
    i = 1
    while i != len( c ):
        if digits[ c[ i ] ] != digit0:
            return False
        i += 1
    return True

combinations0 = [(0, 1), (0, 2), (1, 2)]
combinations = list( itertools.combinations( range( 0, 3 ), 2 ) )
assert( combinations == combinations0 )

assert( isMatch( '121', combinations0[ 1 ] ) )
assert( not isMatch( '121', combinations0[ 0 ] ) )

def matchH( ps, c ):
    RANGES = range( 0, len( ps[ 0 ] ) )
    notC = [ i for i in RANGES if i not in c ]
    digitsMatches = [ i for i in range( 0, len( ps ) ) if isMatch( ps[ i ], c ) ]
    otherDigits = dict()
    for i in digitsMatches:
        keys = ( ps[ i ][ j ] for j in notC )
        key = ''.join( map( str, keys ) )
        if key in otherDigits.keys():
            otherDigits[ key ].append( i )
        else:
            otherDigits[ key ] = [ i ]
    maximum = 0
    maximumI = 0
    for key in otherDigits.keys():
        if maximum < len( otherDigits[ key ] ):
            maximum = len( otherDigits[ key ] )
            maximumI = otherDigits[ key ][ 0 ]
 # the digits of the lowest integer matching the most frequent pattern and the number of matches
    return { 'lowest':ps[ maximumI ], 'matches':maximum }

ps0 = [ '121', '123', '131', '323' ]
matchH0 = {'lowest': '121', 'matches': 2}
assert( matchH( ps0, (0, 2) ) == matchH0 )

primes = list( map( str, euler.readPrimes() ) )
MAX_PRIME_DIGITCOUNT = len( primes[-1] ) # complete set of primes up to MAX_PRIME_DIGITCOUNT digits

def lowestMatch( match ):
    digitCount = 1
    while digitCount < MAX_PRIME_DIGITCOUNT:
        ps = [ p for p in primes if len( p ) == digitCount ]
        for r in range( 1, digitCount ):
            for c in itertools.combinations( range( 0, digitCount ), r ):
                matchh = matchH( ps, c )
                if matchh[ 'matches' ] >= match:
                    return int( ''.join( map( str, matchh[ 'lowest' ] ) ) )
        digitCount += 1
  
print( lowestMatch( 6 ) ) # == 13 
print( lowestMatch( 7 ) ) # == 56003 
print( lowestMatch( 8 ) ) # == 121313      