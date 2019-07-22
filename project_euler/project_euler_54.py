#!/usr/bin/python

import collections

def sortHandDescending( valueKey2count ):
    valueKeysDescending = []
    d = {}
    for valueKey in valueKey2count.keys():
        count = valueKey2count[ valueKey ]
        if count in d:
            d[ count ].append( valueKey )
        else:
            d[ count ] = [ valueKey ]
    counts = list( d.keys() )
    counts.sort( reverse = True )
    for count in counts:
        valueKeys = d[ count ]
        valueKeys.sort( reverse = True )
        for valueKey in valueKeys:
            for i in range( 0, count ):
                valueKeysDescending.append( valueKey )
    return valueKeysDescending
        
VALUES = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ]
VALUE_KEY = {}
for i in range( 0 , len( VALUES ) ):
    VALUE_KEY[ VALUES[ i ] ] = i
VALUE_KEY[ 'T' ] = VALUE_KEY[ '10' ] # Idiocy of a single digit 10 = T

for value in VALUES:
    assert( VALUES[ VALUE_KEY[ value ] ] == value )

def cards( hand_c ):
    cards = hand_c.split( ' ' )
    assert( len( cards ) == 5 )
    return cards

assert( cards( '5H 10C 6S 7S KD' ) == [ '5H', '10C', '6S', '7S', 'KD' ] )

def valueKey( card ):
    return VALUE_KEY[ card[ :-1 ] ]

def valueKeysDescending( hand_c ):
    valueKeys = list( map (valueKey, cards( hand_c ) ) )
    valueKeys.sort( reverse = True )
    return valueKeys

valueKeys0 = [ 11, 8, 5, 4, 3 ]
assert( valueKeysDescending( '5H 10C 6S 7S KD' ) == valueKeys0 )

def onePair( hand_c ):
    valueKeys = valueKeysDescending( hand_c )
    c = collections.Counter( valueKeys )
    c2 = collections.Counter( c.values() )
    if c2[ 2 ] == 1 and c2[ 1 ] == 3:
        return sortHandDescending( c )
    return False

assert( onePair ( '7H 5C 6S 7S 8D' ) == [ 5, 5, 6, 4, 3 ])
assert( not onePair ( '5H 10H 6H 7H KH' ) )

def twoPairs( hand_c ):
    valueKeys = valueKeysDescending( hand_c )
    c = collections.Counter( valueKeys )
    c2 = collections.Counter( c.values() )
    if c2[ 2 ] == 2 and c2[ 1 ] == 1:
        return sortHandDescending( c )
    return False

assert( twoPairs ( '7H 5C 5S 7S 8D' ) == [ 5, 5, 3, 3, 6 ] )
assert( not twoPairs ( '5H 10H 6H 7H KH' ) )

def threeOfAKind( hand_c ):
    valueKeys = valueKeysDescending( hand_c )
    c = collections.Counter( valueKeys )
    c2 = collections.Counter( c.values() )
    if c2[ 3 ] == 1 and c2[ 1 ] == 2:
        return sortHandDescending( c )
    return False

assert( threeOfAKind ( '5H 5C 5S 7S 8D' ) == [ 3, 3, 3, 6, 5 ] )
assert( not threeOfAKind ( '5H 10H 6H 7H KH' ) )

def straight( hand_c ):
    valueKeys = valueKeysDescending( hand_c )
    if all( [ valueKeys[ 0 ] - valueKeys[ i ] == i for i in range( 1, 5 ) ] ):
        return valueKeys
    return False
    
assert( straight ( 'JH 10C 9S QS KD' ) == [ 11, 10, 9, 8, 7 ] )
assert( not straight ( 'JH 8C 9S QS KD' ) )
   
def flush( hand_c ):
    suits = [ card[ -1 ] for card in cards( hand_c ) ]
    if all( suit == suits[ 0 ] for suit in suits ):
        return valueKeysDescending( hand_c )
    return False

assert( flush ( '5H 10H 6H 7H KH' ) == [ 11, 8, 5, 4, 3 ] )
assert( not flush ( '5H 10C 6S 7S KD' ) )

def fullHouse( hand_c ):
    valueKeys = valueKeysDescending( hand_c )
    c = collections.Counter( valueKeys )
    c2 = collections.Counter( c.values() )
    if c2[ 2 ] == 1 and c2[ 3 ] == 1:
        return sortHandDescending( c )
    return False

assert( fullHouse ( '5H 5C 5S 7S 7D' ) == [ 3, 3, 3, 5, 5 ] )
assert( not fullHouse ( '5H 10H 6H 7H KH' ) )

def fourOfAKind( hand_c ):
    valueKeys = valueKeysDescending( hand_c )
    c = collections.Counter( valueKeys )
    c2 = collections.Counter( c.values() )
    if c2[ 4 ] == 1 and c2[ 1 ] == 1:
        return sortHandDescending( c )
    return False

assert( fourOfAKind ( '5H 5C 5S 7S 5D' ) == [ 3, 3, 3, 3, 5 ] )
assert( not fourOfAKind ( '5H 10H 6H 7H KH' ) )

def straightFlush( hand_c ):
    if flush( hand_c ) and straight( hand_c ):
        return valueKeysDescending( hand_c )
    return False
    
assert( straightFlush ( 'JH 10H 9H QH KH' ) == [ 11, 10, 9, 8, 7 ] )
assert( not straightFlush ( 'JH 10H 9D QH KH' ) )
assert( not straightFlush ( '5H 10H 6H 7H KH' ) )
   
def royalFlush( hand_c ):
    if flush( hand_c ) and valueKeysDescending( hand_c ) == [ 12, 11, 10, 9, 8 ]:
        return valueKeysDescending( hand_c )
    return False
    
assert( royalFlush ( 'JH 10H AH QH KH' ) == [ 12, 11, 10, 9, 8 ] )
assert( not royalFlush ( 'JH 10H AD QH KH' ) )
assert( not royalFlush ( '5H 10H 6H 7H KH' ) )
   
RANKS = [ royalFlush, straightFlush, fourOfAKind, fullHouse, flush, straight, threeOfAKind, twoPairs, onePair, valueKeysDescending ]
RANK_KEY = {}
for i in range( 0 , len( RANKS ) ):
    RANK_KEY[ RANKS[ i ] ] = i

for rank in RANKS:
    assert( RANKS[ RANK_KEY[ rank ] ] == rank )

def cmp_poker( a, b ):
# -1 / 0 / +1 = Player 1 loses / draws / wins
    for rank in RANKS:
        ra = rank( a )
        rb = rank( b )
        if not ra and rb:
            return -1
        elif ra and not rb:
            return +1
        elif ra and rb: # The hands have the same rank. The card values decide.
            if ra < rb:
                return -1
            elif rb < ra:
                return +1
    return 0

assert( cmp_poker( '5H 5C 6S 7S KD', '2C 3S 8S 8D TD' ) == -1 )
assert( cmp_poker( '5D 8C 9S JS AC', '2C 5C 7D 8S QH' ) == +1 )
assert( cmp_poker( '2D 9C AS AH AC', '3D 6D 7D TD QD' ) == -1 )
assert( cmp_poker( '4D 6S 9H QH QC', '3D 6D 7H QD QS' ) == +1 )
assert( cmp_poker( '2H 2D 4C 4D 4S', '3C 3D 3S 9S 9D' ) == +1 )

with open( 'Data/p054_poker.txt', 'r' ) as myfile:
    lines = myfile.read().splitlines()

count = 0
for line in lines:
    cs = line.split(' ')
    a = ' '.join(cs[ :5 ])
    b = ' '.join(cs[ 5: ])
    if cmp_poker( a , b ) == +1:
        count += 1
print( count )