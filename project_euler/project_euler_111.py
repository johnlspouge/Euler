#!/usr/bin/python

from collections import Counter
from itertools import combinations, product
from euler import readPrimes, isPrime
from copy import deepcopy

primes = readPrimes() # complete set of primes up to 15485863 digits
primea = set( primes )
DIGIT_BIG = 7

BASE = 10
DIGIT_S = range( 0, BASE )

# Does the list of digits match in the positions indexed by c?
def primesWithDigitCount( d ):
    return [ str( p_i ) for p_i in primes if BASE**(d - 1) <= p_i < BASE**d ]

def toDigit2Count( prime_c ):
    return Counter( list( prime_c ) )

c0 = Counter( {'6': 2, '8': 2, '4': 1, '5': 1, '2': 1} )
assert( toDigit2Count( '4656882' ) == c0 )

def primeWithRepeat_is( numberOfDigits_i, digit_i ):
    digitOther_is = list( DIGIT_S )
    digitOther_is.remove( digit_i )
    repeat_is = [ digit_i for i in range( 0, numberOfDigits_i ) ]
    for nonRepeats_i in range( 0, numberOfDigits_i ):
        if nonRepeats_i == 0 and numberOfDigits_i % 2 == 0:
            continue
        candidate_is = []
        for c in combinations( range( 0, numberOfDigits_i ), nonRepeats_i ):
            if c[ 0 ] != 0 and digit_i == 0:
                continue
            for c1 in product( digitOther_is, repeat = nonRepeats_i ):
                if c[ 0 ] == 0 and c1[ 0 ] == 0:
                    continue
                c0 = list( deepcopy( repeat_is ) )
                assert( len( c0 ) == numberOfDigits_i )
                assert( len( c ) == nonRepeats_i )
                for j in range( 0, len( list( c ) ) ):
                    c0[ c[ j ] ] = c1[ j ]
                primeMaybe = int( ''.join( map( str, c0 ) ) )
                candidate_is.append( primeMaybe )
                    #print( c, i, c0, j, primeMaybe)
        primeWithRepeat_is = []
        for candidate_i in candidate_is:
            if numberOfDigits_i < DIGIT_BIG and candidate_i in primea:
                primeWithRepeat_is.append( candidate_i )
            elif DIGIT_BIG <= numberOfDigits_i and isPrime( candidate_i, primes ):
                primeWithRepeat_is.append( candidate_i )
        if len( primeWithRepeat_is ) != 0:
            break
    return digit_i, numberOfDigits_i - nonRepeats_i, len( primeWithRepeat_is ), sum( primeWithRepeat_is )

prime_is = primeWithRepeat_is( 4, 5 )                
assert( prime_is == ( 5, 3, 1, 5557 ) )                      
prime_is = primeWithRepeat_is( 4, 3 )
assert( prime_is == ( 3, 3, 12, 46214 ) )
sum_i = 0 
for digit_i in range( 0, 10 ):
    prime_is = primeWithRepeat_is( 4, digit_i )
    sum_i += prime_is[ 3 ]
    #print( prime_is[ 3 ] )             
assert( sum_i == 273700 )

sum_i = 0 
for digit_i in range( 0, 10 ):
    prime_is = primeWithRepeat_is( 10, digit_i )
    sum_i += prime_is[ 3 ]             
assert( sum_i == 612407567715 )

