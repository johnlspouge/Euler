#!/usr/bin/python

N = 100000 # N = 10 # 10e5
BASE = 10
DIGITS = list(range(1,BASE))

maximum = 0
for i in range(1,N): #
    for j in range(2,BASE): # multipliers in (1...j)
        s = ""
        for k in range(1,j+1): # multipliers in (1...j)
            s += str(i * k)
            digits = list(map(int, list(s)))
            digits.sort()
            if digits == DIGITS:
                pandigital = int(s)
                if (maximum < pandigital):
                    maximum = pandigital

print(maximum)