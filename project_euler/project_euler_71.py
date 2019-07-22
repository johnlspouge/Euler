#!/usr/bin/python

D = 10**6 # D = 8 # 
minimum = 1.0

for b in range( 1, D + 1 ):
    a = int( 3 * b / 7 )
    delta = 3 / 7 - a / b
    assert( 0.0 <= delta )
    if 0.0 < delta < minimum:
        minimum = delta
        aMinimum = a

print( aMinimum )