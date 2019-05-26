#!/usr/bin/python

K = 20
N = 2 * K
comb = 1
k = 1
while k <= K:
    comb *= N - k + 1
    comb //= k
    k += 1

print(comb)
