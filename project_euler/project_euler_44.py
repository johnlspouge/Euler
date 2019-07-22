#!/usr/bin/python

from math import sqrt

def isPentagonal(number):
    EPS = 1.0e-10
    n = int((1 + EPS) * (1 + sqrt(1 + 24 * number)) / 6)
    if n * (3 * n - 1) // 2 == number:
        return True
    return False

assert(isPentagonal(145))
assert(not isPentagonal(27))

def pentagonal(n):
    return n * (3 * n - 1) // 2

assert(pentagonal(3) == 12)

p0 = 1
p1 = 5
pentagonals = [p0, p1]

d = 0 # smallest pentagonal 
n = 3 # index in pentagonals
while d == 0 or p1 - p0 > d:
    p2 = pentagonal(n) # next pentagonal
    assert(isPentagonal(p2))
    for p in pentagonals:
        pTest = p2 - p
        if isPentagonal(pTest) and isPentagonal(p2 + pTest):# 4 pentagonals
            d = p
            print(n, p, pTest, p2, p2 + pTest)
            pentagonals = [p for p in pentagonals if p < d]
    if d == 0:
        pentagonals.append(p2)
    p0 = p1
    p1 = p2
    n += 1

print(d)
