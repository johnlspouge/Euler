#!/usr/bin/python

def isPandigital( digits_i ):
    digits_cs = list( str( digits_i ) )
    return '0' not in digits_cs and len(digits_cs) == 9 and len(set(digits_cs)) == 9

assert( isPandigital( 123456987 ) )
assert( not isPandigital( 123456977 ) )
assert( not isPandigital( 123456087 ) )

def nextTwoFibonaccis( f0, f1 ):
    return f1, f0 + f1

assert( ( 1, 2 ) == nextTwoFibonaccis( 1, 1 ) )
assert( ( 2, 3 ) == nextTwoFibonaccis( 1, 2 ) )
assert( ( 5, 8 ) == nextTwoFibonaccis( 3, 5 ) )

def isFirstPandigital( n ):
    return isPandigital( n % 10**9 )

i = 2
f0, f1 = 1, 1
while not isFirstPandigital( f1 ):
    f0, f1 = nextTwoFibonaccis( f0, f1 )
    i += 1
    
assert( i == 541 )

def isLastPandigital( n ):
    while 10**9 <= n:
        n //= 10
    return isPandigital( n )

i = 2
f0, f1 = 1, 1
while not isLastPandigital( f1 ):
    f0, f1 = nextTwoFibonaccis( f0, f1 )
    i += 1
    
assert( i == 2749 )

i = 2
f0, f1 = 1, 1
while not isFirstPandigital( f1 ) or not isLastPandigital( f1 ):
    f0, f1 = nextTwoFibonaccis( f0, f1 )
    i += 1
    
assert( i == 329468 )
