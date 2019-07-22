#!/usr/bin/python

#import scipy.special

#print (scipy.special.comb(40,20,exact=True))

K = 20
N = 2 * K
c = 1
k = 1
while k <= K:
    c *= N - k + 1
    c //= k
    k += 1

print(c)
