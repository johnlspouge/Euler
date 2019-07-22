#!/usr/bin/python

BOUND = 100 # upper bound for generating a ** b

s = {} # set of values a ** b

a = 2
while a <= BOUND:
    b = 2
    while b <= BOUND:
        s[a ** b] = True
        b += 1
    a += 1

print(len(s.keys()))                
