#!/usr/bin/python

def isDigitCancelingTopRight(a, b, c):
    return a != 0 != b and (10 * a + b) * c == a * (10 * b + c)

def isDigitCancelingTopLeft(a, b, c):
    return a != 0 != b and (10 * b + a) * c == a * (10 * c + b)

digitCanceling = []

a = 0
while a < 10:
    c = a + 1
    while c < 10:
        b = 0
        while b < 10:
            if isDigitCancelingTopRight(a, b, c):
                digitCanceling.append([a, b, c])
            b += 1
        c += 1
    a += 1

print(digitCanceling) # [[1, 6, 4], [1, 9, 5], [2, 6, 5], [4, 9, 8]]
# answer = 100