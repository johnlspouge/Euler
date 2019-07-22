#!/usr/bin/python

from math import factorial
from euler import appendDigits

numberIsSumDigitFactorials = []

a = 3
while a < 10000000:
    digits = []
    appendDigits(a, digits)
    factorials = map(factorial, digits)
    if a == sum(factorials):
        numberIsSumDigitFactorials.append(a)
    a += 1

print(numberIsSumDigitFactorials) # [145, 40585]
print(sum(numberIsSumDigitFactorials)) # 40730