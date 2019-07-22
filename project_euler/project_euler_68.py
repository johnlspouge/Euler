#!/usr/bin/python

from itertools import permutations
from string import digits
import numpy as np

LINES = [ [ 0, 1, 2 ], [ 3, 2, 4 ], [ 5, 4, 6 ], [ 7, 6, 8 ], [ 9, 8, 1 ] ]
FIVE = len( LINES )
EXTERNALS = [ line[ 0 ] for line in LINES ]
DIGITS = list( map( int, list( digits ) ) )

def isTenExternal( ns ):
    i = ns.index( 9 )
    return i in EXTERNALS

def isMinimumExternalAt0( ns ):
    i = np.argmin( [ ns[ j ] for j in EXTERNALS ] )
    return i == 0

def sumLine( ns, line ):
    s = 0
    for i in line:
        s += ns[ i ]
    return s

def isEverySumEqual( ns ):
    s = sumLine( ns, LINES[ 0 ] )
    for i in range( 1, len( LINES ) ):
        s0 = s
        s = sumLine( ns, LINES[ i ] )
        if s != s0:
            return False
    return True

def string( ns ):
    sc = ''
    for line in LINES:
        for vertex in line: 
            sc += str( ns[ vertex ] + 1 )
    return sc
    
maxString = 0 
for ns in permutations( DIGITS ):
    if isTenExternal( ns ) and isMinimumExternalAt0( ns ) and isEverySumEqual( ns ):
        m = int( string( ns ) )
        if maxString < m:
            maxString = m

assert( maxString == 6531031914842725 )            
