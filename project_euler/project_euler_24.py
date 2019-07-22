#!/usr/bin/python

from itertools import permutations as permutations

n = 10
number = 1000000

perm = list(permutations(range(0, n)))
s = str(perm[number - 1])
print(s.replace(', ', '').replace('(', '').replace(')', ''))
