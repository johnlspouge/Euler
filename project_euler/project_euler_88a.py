#!/usr/bin/python

from euler import readPrimes, primeFactors, primePowerFactorization
from functools import reduce
from operator import mul, add
from itertools import combinations_with_replacement
from copy import deepcopy 
from functools import cmp_to_key

UPPER = 2 * 12000
PRIMES = readPrimes( UPPER )

def cmpFactor2Powers( factor2powers, factor2powers0 ):
    factors = sorted( factor2powers.keys() )
    values = [ factor2powers[ factor ] for factor in factors ]
    factors0 = sorted( factor2powers0.keys() )
    values0 = [ factor2powers0[ factor0 ] for factor0 in factors0 ]
    for i in range( 0, min( len( factors ), len( factors0 ) ) ):
        if factors[ i ] < factors0[ i ]:
            return -1
        if factors[ i ] > factors0[ i ]:
            return +1
        if values[ i ] < values0[ i ]:
            return -1
        if values[ i ] > values0[ i ]:
            return +1
    if len( factors ) < len( factors0 ):
        return -1
    if len( factors ) > len( factors0 ):
        return +1
    return 0

def uniqueFactor2Powers( factor2powers_ ):
    factor2powers0 = sorted( factor2powers_, key=cmp_to_key( cmpFactor2Powers ) )
    factor2powers = [ factor2powers0[ 0 ] ]
    for i in range( 1, len( factor2powers0 ) ):
        if cmpFactor2Powers( factor2powers0[ i ], factor2powers0[ i - 1 ] ) != 0:
            factor2powers.append( factor2powers0[ i ] )
    return factor2powers

assert( len( uniqueFactor2Powers( [ {12: 1}, {12: 1} ] ) ) == 1 )

def toK( factor2power ):
    n = reduce( mul, [ factor**factor2power[ factor ] for factor in factor2power.keys() ]  )
    s = reduce( add, [ factor * factor2power[ factor ] for factor in factor2power.keys() ] )
    j = reduce( add, [ factor2power[ factor ] for factor in factor2power.keys() ] )
    return n - s + j

assert( toK( {2:3} ) == 5 )
assert( toK( {2:1,4:1} ) == 4 )
assert( toK( {4:2} ) == 10 )

def ka( n ):
    factor2powers = list()
    factor2power = primePowerFactorization( primeFactors( n, PRIMES ) )
    factor2powers.append( factor2power )
    #print( factor2powers )
    ka = set()
    ka.add( toK( factor2power ) )
    j = reduce( add, [ factor2power[ factor ] for factor in factor2power.keys() ] ) # # of factors in n
    while j > 0:
        factor2powers0 = deepcopy( factor2powers )
        k2factor2powers = dict({})
        for factor2power0 in factor2powers0:
            for factors in combinations_with_replacement( factor2power0.keys(), 2 ):
                if factors[ 0 ] == factors[ 1 ] and factor2power0[ factors[ 0 ] ] == 1:
                    continue
                else:
                    factor2power = deepcopy( factor2power0 )
                    factor = factors[ 0 ] * factors[ 1 ]
                    for i in [0, 1]:
                        factor2power[ factors[ i ] ] -= 1
                        if factor2power[ factors[ i ] ] == 0:
                            del factor2power[ factors[ i ] ]
                    if factor in factor2power.keys():
                        factor2power[ factor ] += 1
                    else:
                        factor2power[ factor ] = 1
                    k = toK( factor2power )
                    if k in k2factor2powers:
                        k2factor2powers[ k ].append( factor2power )
                    else:
                        k2factor2powers[ k ] = [ factor2power ]
        factor2powers = list()
        for k in k2factor2powers.keys():
            ka.add( k )
            factor2powers.extend( uniqueFactor2Powers( k2factor2powers[ k ] ) )
        #print( factor2powers )
        j -= 1
    return ka

assert( ka( 8 ) == { 1, 4, 5 } )
assert( ka( 12 ) == { 1, 6, 7, 8 } )

def k2minimumN( upper ):
    ka0 = set( range( 2, upper ) )
    k2minimumN = dict({})
    for n in range( 2, 2 * upper - 1 ):
        #if n % 1000 == 0:
            #print( n )
        for k in ka( n ):
            if 1 < k < upper and k not in k2minimumN.keys():
                k2minimumN[ k ] = n
                ka0.remove( k )
                if len( ka0 ) == 0:
                    return k2minimumN
    return k2minimumN

upper = 7
d = k2minimumN( upper )
minimumNa = set( [ d[ k ] for k in list( range( 2, upper ) ) ] )
assert( sum( minimumNa ) == 30 )

upper = 13
d = k2minimumN( upper )
minimumNa = set( [ d[ k ] for k in list( range( 2, upper ) ) ] )
assert( sum( minimumNa ) == 61 )

upper = 12001
d = k2minimumN( upper )
minimumNa = set( [ d[ k ] for k in list( range( 2, upper ) ) ] )
assert( sum( minimumNa ) == 7587457 )
