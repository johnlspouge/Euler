#!/usr/bin/python

import itertools

DIGITS = list( map( int, range( 0, 10 ) ) )
OPERATIONS = [ '+' , '-' , '*', '/' ]

# 1,2,...,count are in targeta, but count + 1 is not in targeta.
def countConsecutive( targeta ):
    count = 0
    while count + 1 in targeta:
        count += 1
    return count

assert( countConsecutive( set( [1,2,3,5,7] ) ) == 3 )

# 1,2,...,count are in targeta, but count + 1 is not in targeta.
def operation( a, op, b  ):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError()
        return a / b
    else:
        raise Exception('Impossible operation')

assert( operation( 2, '+', 3  ) == 5 )
assert( operation( 2, '-', 3  ) == -1 )
assert( operation( 2, '*', 3  ) == 6 )
assert( operation( 2, '/', 3  ) == 2 / 3 and int( 2 / 3 ) != 2 / 3 )
        
def rounded( result ):
    EPS = 1.0e-06
    if EPS <= abs( result - int( result ) ):
        return 0 # not an integer result, so set to 0     
    return int( result )
    
def result( ds, ops ):
    while len( ops ) != 0:
        assert( len( ds ) == 1 + len( ops ) )
        ds[ 0 ] = operation( ds.pop( 0 ), ops.pop( 0 ), ds[ 0 ] )
    return rounded( ds[ 0 ] )

assert( result( [ 1, 3, 4, 2 ], list( '+*/' ) ) == 8 )
assert( result( [ 1, 2, 3, 4 ], list( '/+*' ) ) == 14 )
assert( result( [ 2, 3, 4, 1 ], list( '+*-' ) ) == 19 )
assert( result( [ 1, 2, 4, 3 ], list( '+**' ) ) == 36 )

def resultPaired( ds, ops ):
    d0 = operation( ds[ 0 ], ops[ 0 ], ds[ 1 ] )
    d1 = operation( ds[ 2 ], ops[ 2 ], ds[ 3 ] )
    d2 = operation( d0, ops[ 1 ], d1 )
    return rounded( d2 )

assert( resultPaired( [ 1, 3, 4, 2 ], list( '+*/' ) ) == 8 )
assert( resultPaired( [ 1, 2, 3, 4 ], list( '/+*' ) ) == 0 )
assert( resultPaired( [ 2, 3, 4, 1 ], list( '+*-' ) ) == 15 )
assert( resultPaired( [ 1, 2, 4, 3 ], list( '+**' ) ) == 36 )

# Calculates the targets and then counts consecutive targets.
def countConsecutiveTargets( ns ):
    targeta = set( [] )
    for ds in itertools.permutations( ns ): 
        for op in itertools.product( OPERATIONS, repeat = 3 ):
            try:
                targeta.add( result( list( ds ), list( op ) ) )
            except ZeroDivisionError:
                pass
            try:
                targeta.add( resultPaired( list( ds ), list( op ) ) )
            except ZeroDivisionError:
                pass
    return countConsecutive( targeta )

assert( countConsecutiveTargets( range( 1, 5 ) ) == 28 )
assert ( countConsecutiveTargets( [ 1, 2, 5, 6 ] ) == 43 )

def targetc():
    sc = ''
    count = 0
    for ns in itertools.combinations( DIGITS, 4 ): 
        count0 = countConsecutiveTargets( ns )
        if count < count0:
            count = count0
            ns = list( ns )
            ns.sort()
            nsc = list( map( str, ns ) )
            sc = ''.join( nsc )
    return sc
            
assert( targetc() == '1258' )
