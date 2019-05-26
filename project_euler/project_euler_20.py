#!/usr/bin/python

N = 100

def digitSum(n, base = 10):
    sum = 0
    while n > 0:
        sum += n % base
        n //= base
    return sum

def factorial(n):
    f = 1
    i = 1
    while i <= n:
        f *= i
        i += 1
    return f

print(digitSum(factorial(N)))