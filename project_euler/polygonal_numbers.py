#!/usr/bin/python

from math import sqrt

EPS = 1.0e-10

def triangle(n):
    return n * (n + 1) // 2

def triangleInverse(number):
    return int((1 + EPS) * (-1 + sqrt(1 + 8 * number)) / 2)

def isTriangle(number):
    return triangle(triangleInverse( number )) == number

assert(isTriangle(15))
assert(not isTriangle(18))

def square(n):
    return n * n

def squareInverse(number):
    return int( (1 + EPS) * sqrt(number) )

def isSquare(number):
    return square(squareInverse(number)) == number

assert(isSquare(16))
assert(not isSquare(24))

def pentagonal(n):
    return n * (3 * n - 1) // 2

def pentagonalInverse(number):
    return int((1 + EPS) * (1 + sqrt(1 + 24 * number)) / 6)

def isPentagonal(number):
    return pentagonal(pentagonalInverse(number)) == number

assert(isPentagonal(145))
assert(not isPentagonal(27))

def hexagonal(n):
    return n * (2 * n - 1)

def hexagonalInverse(number):
    return int((1 + EPS) * (1 + sqrt(1 + 8 * number)) / 4)

def isHexagonal(number):
    return hexagonal(hexagonalInverse(number)) == number

assert(isHexagonal(15))
assert(isHexagonal(45))
assert(not isHexagonal(48))

def heptagonal(n):
    return n * (5 * n - 3) // 2

assert(heptagonal(4) == 34)
assert(heptagonal(5) == 55)

def heptagonalInverse(number):
    return int((1 + EPS) * (3 + sqrt(9 + 40 * number)) / 10)

def isHeptagonal(number):
    return heptagonal(heptagonalInverse(number)) == number

assert(isHeptagonal(34))
assert(not isHeptagonal(54))

def octagonal(n):
    return n * (3 * n - 2)

assert(octagonal(4) == 40)
assert(octagonal(5) == 65)

def octagonalInverse(number):
    return int((1 + EPS) * (1 + sqrt(1 + 3 * number)) / 3)

def isOctagonal(number):
    return octagonal(octagonalInverse(number)) == number

assert(isOctagonal(40))
assert(not isOctagonal(64))

polygonal = {3:triangle,4:square,5:pentagonal,6:hexagonal,7:heptagonal, 8:octagonal}

assert(polygonal[ 3 ]( 4 ) == 10 )

polygonalInverse = {3:triangleInverse,4:squareInverse,5:pentagonalInverse,6:hexagonalInverse,7:heptagonalInverse,8:octagonalInverse}

assert(polygonalInverse[ 3 ]( 15 ) == 5 )
assert(polygonalInverse[ 3 ]( 16 ) == 5 )

def uniquePolygon(number):
    a = set()
    if isTriangle(number):
        a.add(3)
    if isSquare(number):
        a.add(4)
    if isPentagonal(number):
        a.add(5)
    if isHexagonal(number):
        a.add(6)
    if isHeptagonal(number):
        a.add(7)
    if isOctagonal(number):
        a.add(8)
    if len(a) == 1:
        n = a.pop()
        return n
    return 0
    
assert( uniquePolygon(16) == 4 )
assert( not uniquePolygon(15) ) # {3,8}
assert( not uniquePolygon(13) ) # 0
