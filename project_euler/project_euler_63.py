#!/usr/bin/python

c = 0

n = 1
while True: # # of digits
    d = [ 1 for i in range( 1, 10 ) if 10**(n - 1) <= i**n < 10**n ]
    s = sum( d )
    if s == 0:
        break
    c += s
    n += 1
    
print( c )
