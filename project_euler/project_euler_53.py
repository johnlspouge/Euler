#!/usr/bin/python

import math

THRESHOLD = 10**6

# Sorts the digits of nstr in ascending order.
def pascal( n, k ):
    return math.factorial( n ) // math.factorial( k ) // math.factorial( n - k )

count = 0
for n in range(0, 101):
    for k in range(0, n):
        if THRESHOLD < pascal( n, k ):
            count += 1
            
print( count )        