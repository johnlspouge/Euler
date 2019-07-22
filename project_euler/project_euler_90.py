#!/usr/bin/python

from string import digits
from itertools import combinations, product
from copy import deepcopy
from functools import reduce

FACE_COUNT = 6 # number of faces

squares = set( ['01','04','06','16','25','36','46','64','81'] )

possibles = [ [ set(), set() ] ] # list of pair of empty sets

for square in squares:
    possibles0 = possibles
    possibles = [] 
    for possible0 in possibles0:
        for j in [ 0, 1 ]:
            possible = deepcopy( possible0 )
            possible[ (0 + j) % 2 ].add( square[ 0 ] )
            possible[ (1 + j) % 2 ].add( square[ 1 ] )
            if all( len( p ) <= FACE_COUNT for p in possible ):
                possibles.append( possible )

# Every dice with faces [0...8] satisfying the constraints contains at least one pair of sets in possibles.            
# The faces do not yet account for 6 == 9.
            
nines = []           
for possible in possibles:
    for i in [ 0, 1 ]:
        if '6' in possible[ i ]:
            possible0 = deepcopy( possible )
            possible0[ i ].remove( '6' )
            possible0[ i ].add( '9' )
            nines.append( possible0 )
    if '6' in possible[ 0 ] and '6' in possible[ 1 ]:
        possible0 = deepcopy( possible )
        for i in [ 0, 1 ]:
            possible0[ i ].remove( '6' )
            possible0[ i ].add( '9' )
            nines.append( possible0 )

possibles.extend( nines )            

# Every dice with faces [0...9] satisfying the constraints contains at least one pair of sets in possibles.            
# The faces now include 9.            

def clean( dice ):
    for i in [ 0, 1 ]:
        dice[ i ] = list( map( str, list( dice[ i ] ) ) )
        dice[ i ].sort()
        dice[ i ] = ''.join( dice[ i ] )
    dice.sort()
    return dice

assert( clean( [ { 3, 1, 2 }, { 6, 5, 4 } ] )  == [ '123', '456' ] )

# Add all possible faces to all possibles.            

digita = set( list( digits ) )
DIGIT_COUNT = len( digita ) # distinct digits [0...9]

dices = []
for possible in possibles:
    others = [ digita.difference( p ) for p in possible ]
    combs = reduce( product, [ combinations( others[ i ], FACE_COUNT - len( possible[ i ] ) ) for i in [ 0, 1 ] ] )
    for ns in combs:
        dice = deepcopy( possible )
        dice = [ dice[ i ].union( ns[ i ] ) for i in [ 0, 1 ] ]
        dices.append( clean( dice ) )

dicea = set( map( tuple, dices ) )

assert( len( dicea ) == 1217 )
