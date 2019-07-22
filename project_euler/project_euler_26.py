#!/usr/bin/python

N = 1000 
TEN = 10

def cycle(denominator):
    list = []
    dict = {}
    remainder = TEN

    i = 0
    while remainder not in dict: 
        remainder %= denominator
        list.append(remainder)
        if remainder in dict:
            break
        else:
            dict[remainder] = i
        remainder *= TEN
        i += 1
        
    return i - dict[remainder]

max = 0
argmax = 0
n = 1
while n != N:
    if max < cycle(n):
        max = cycle(n)
        argmax = n
    n += 1

#print(max)
print(argmax)
