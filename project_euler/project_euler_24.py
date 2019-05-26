#!/usr/bin/python

import math

N = 1000

phi = (1+math.sqrt(5.0))/2.0

print(1 + int((N - 1 + math.log10(5.0) / 2.0)/math.log10(phi)))