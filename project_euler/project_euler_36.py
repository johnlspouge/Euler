#!/usr/bin/python

from copy import copy
from euler import appendDigitsUnsorted

N = 1000000 # N = 100 # 
# BASE = 10

def isDigitPalindrome(n, d = [], base = 10):
    d = appendDigitsUnsorted(n, d, base)
    r = copy(d)
    r.reverse()
    return d == r

palindrome = []
a = 1
while a < N:
    if isDigitPalindrome(a, [], 10) and isDigitPalindrome(a, [], 2):
        palindrome.append(a)
    a += 1

print(palindrome) # [1, 3, 5, 7, 9, 33, 99]
# [1, 3, 5, 7, 9, 33, 99, 313, 585, 717, 7447, 9009, 15351, 32223, 39993, 53235, 53835, 73737, 585585]
print(sum(palindrome)) # 157
# 872187
