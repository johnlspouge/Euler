#!/usr/bin/python

N = 1000 
TEN = 10

zero = [0,3,3,5,4,4,3,5,5,4] # zero,one,...,nine
teen = [3,6,6,8,8,7,7,9,8,8] # ten,eleven,...,nineteen
two  = [0,3,6,6,5,5,5,7,6,6] # zero,ten,twenty,...,ninety

AND = 3
HUNDRED = 7
ONE_THOUSAND = 3 + 8

def count(i):
    count = 0
    place = 0
    while i != 0:
        if place == 0:
            d0 = i % TEN
            place += 1
            i //= TEN
            d1 = i % TEN
            if d1 == 0:
                count += zero[d0]
            elif d1 == 1:
                count += teen[d0]
            else:
                count += two[d1] + zero[d0]
        elif place == 2:
            d = i % TEN
            if count != 0:
                count += AND
            count += zero[d] + HUNDRED
        else:
            raise ValueError('Number is too large.')
        place += 1
        i //= TEN
    
    return count

countLetter = 0
n = 1
while n < N:
    countLetter += count(n)
    n += 1

countLetter += ONE_THOUSAND    
print(countLetter)
