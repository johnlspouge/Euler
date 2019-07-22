#!/usr/bin/python

from math import sqrt

P = 1001 # maximum perimeter # P = 130 #
count = {}

for a in range(1, P): 
    for b in range(a + 1, P - 2 * a):
        c = sqrt(a*a + b*b)
        if c == int(c):
            c = int(c)
            p = a + b + c
            if p > 1000:
                continue
            if p in count:
                count[p] += 1
            else:
                count[p] = 1

print(max(count, key=count.get))