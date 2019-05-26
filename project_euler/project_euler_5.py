#!/usr/bin/python

import math

factors = []

# Returns true if none of the "primes" divides n.
def Is_Prime(primes, n):

    for p in primes:
        if n % p == 0:
            return False;

    return True;

# Multiplies all values in the list.
def multiply(list) : 
      
    product = 1
    for x in list: 
         product *= x  

    return product  
          
f = int(input("inclusive upper bound: "))

primes = []

p = 2
while p <= f:
    if Is_Prime(primes, p):
        primes.append(p)
    p += 1

# primes contains all primes <= f

gcd = 1

for p in primes:
    power = int(math.log(f, p));
    gcd *= p ** power
    
print(gcd)