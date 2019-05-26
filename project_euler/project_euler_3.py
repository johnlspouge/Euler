#!/usr/bin/python

primes = []
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
          
f = int(input("number to factor: "))

p = 2
while p <= f:
    if Is_Prime(primes, p):
        primes.append(p)
        while f % p == 0:
            factors.append(p)
            f /= p
    p += 1
            
print(factors)
print(multiply(factors))