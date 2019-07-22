#!/usr/bin/python

BOUND = 999999 # upper bound
POWER = 5

def sumDigits(number, power, base = 10):
    sum = 0
    while number > 0:
        digit = number % base
        sum += pow(digit, power)
        number //= base
    return sum

s = [] # set of numbers equal to sum of digits' 5-th power

a = 2
while a <= BOUND:
    if sumDigits(a, POWER) == a:
        s.append(a)
    a += 1

print(s)
print(sum(s))
