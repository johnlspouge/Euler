#!/usr/bin/python

pentagonalm = dict( {} )

def pentagonal(k):
    if k in pentagonalm.keys():
        return pentagonalm[ k ]
    else:
        pentagonalm[ k ] = k * (3 * k - 1) // 2
    return pentagonalm[ k ]

pm = dict( { 0:1 } )

def partition( n ): 
    if n in pm.keys():
        return pm[ n ]
    p = 0
    k = 1
    while True:
        m = n - pentagonal( k )
        if m < 0:
            break;
        term = partition( m )
        if k % 2 == 0:
            term = -term
        p += term
        k += 1
    k = -1
    while True:
        m = n - pentagonal( k )
        if m < 0:
            break;
        term = partition( m )
        if k % 2 == 0:
            term = -term
        p += term
        k -= 1
    pm[ n ] = p
    return p

# Tests
    
assert( partition( 1 ) == 1 )
assert( partition( 5 ) == 7 )
assert( partition( 6 ) == 11 )

# Main

assert( partition( 100 ) - 1 == 190569291 )