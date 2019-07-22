#!/usr/bin/python

from scipy.special import comb
from copy import deepcopy

def differences( ns ):
    return [ ns[ i ] - ns[ i - 1 ] for i in range( 1, len( ns ) ) ]

def isConstant( ns ):
    return all( [ n == ns[ 0 ] for n in ns[ 1: ] ] )

def coefficients( ms ):
    ns = deepcopy( ms )
    cs = []
    while len( ns ) != 0:
        cs.append( ns [ 0 ] )            
        ns = differences( ns )
    return cs

cs = coefficients( [ 1, 8, 27, 64 ] )
assert( cs == [1, 7, 12, 6] )

def approx( cs, m ):
    s = 0
    for n in range( 0, m ):
        s += comb( m, n, exact = True ) * cs[ n ]
    return s

bops0 = [ 1, 15, 58 ]
bops = [ approx ( cs, n ) for n in range( 1, 4 ) ]
assert( bops == bops0 ) 
assert( sum( bops ) == 74 )

def polynomial( n ):
    return sum( [ (-n)**k for k in range( 0, 11 ) ] )
    
assert( polynomial( -1 ) == 11 )
assert( polynomial( 0 ) == 1 )  
assert( polynomial( 1 ) == 1 ) 
assert( polynomial( 2 ) == 683 )

ms = [ polynomial( n ) for n in range( 1, 11 ) ]
cs = coefficients( ms )
bops = [ approx ( cs, n ) for n in range( 1, 11 ) ]
assert( sum( bops ) == 37076114526 )   