#!/usr/bin/python

from math import sqrt

def isTriangle(number):
    EPS = 1.0e-10
    n = int((1 + EPS) * (-1 + sqrt(1 + 8 * number)) / 2)
    if n * (n + 1) // 2 == number:
        return True
    return False

assert(isTriangle(15))
assert(not isTriangle(18))

def isPentagonal(number):
    EPS = 1.0e-10
    n = int((1 + EPS) * (1 + sqrt(1 + 24 * number)) / 6)
    if n * (3 * n - 1) // 2 == number:
        return True
    return False

assert(isPentagonal(145))
assert(not isPentagonal(27))

def isHexagonal(number):
    EPS = 1.0e-10
    n = int((1 + EPS) * (1 + sqrt(1 + 8 * number)) / 4)
    if n * (2 * n - 1) == number:
        return True
    return False

assert(isHexagonal(45))
assert(not isHexagonal(48))

def triangle(n):
    return n * (n + 1) // 2

assert(triangle(3) == 6)

n = 286 # index in triangle numbers
while True:
    t = triangle(n)
    if isPentagonal(t) and isHexagonal(t):
        break
    n += 1

print(t)
