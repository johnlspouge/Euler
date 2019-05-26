#!/usr/bin/python

upperBound = int(input("upper bound: "))

n = 1
sum = 0

while n <= upperBound:
    if n % 3 == 0 or n % 5 == 0:
        sum += n
    n += 1
        
print(sum)
