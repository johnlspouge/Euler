#!/usr/bin/python

BASE = 10
D = 6
N = BASE**D

s = ""
for n in range(1,N):
    s += str(n)

product = 1
for i in range(0,D+1):
    product *= int(s[10**i - 1])
    
print(product)