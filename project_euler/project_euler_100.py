#!/usr/bin/python

N = 10**12 # N = 10**2 #

p = 1
q = 1
n = (1 + p) // 2
b = (1 + q) // 2

while n <= N:
    b = (1 + q) // 2
    n = (1 + p) // 2
    p, q = p + 2 * q, p + q
    p, q = p + 2 * q, p + q
        
print( b, n )
