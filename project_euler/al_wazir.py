#!/usr/bin/python

# Returns [0,1,...,2*n-1].
def numbersUpToTwice(n):

    n *= 2
    numbers = []
    i = 0
    while i < n:
        numbers.append(i)
        i += 1

    return numbers

# Returns double factorials less than (2*n-1)!!.
def doubleFactorialsOfTwice(n):

    n *= 2
    n -= 1
    doubleFactorials = []
    i = 1
    product = 1
    while i < n:
        product *= i
        doubleFactorials.append(product)
        i += 2
    
    doubleFactorials.reverse()
    
    return doubleFactorials

# Returns double factorial (2*n-1)!!.
def doubleFactorialOfTwice(n):

    n *= 2
    doubleFactorials = []
    i = 1
    product = 1
    while i < n:
        product *= i
        i += 2
    
    return product

# Returns the combinatorial code for the pairs.
def digitsOfCode(d, numbers, doubleFactorials):
    
    digits = []
    for n in doubleFactorials:
        digits.append(d // n)
        d %= n
        
    return digits

def digits2Pairs(digits, numbers):
    
    numbers0 = list(numbers)
    
    pairs = {} # dictionary
    for d in digits:
        one = numbers0.pop(0)
        two = numbers0.pop(d)
        pairs[one] = two
    
    pairs[numbers0[0]] = numbers0[1]
    
    return pairs

"""
n = 15
#(2n - 1)!! = 6190283353629375
i = 190283353629375
numbers = numbersUpToTwice(n)
doubleFactorials = doubleFactorialsOfTwice(n)
digits = digitsOfCode(i, numbers, doubleFactorials) 
print(i, digits2Pairs(digits, numbers))
"""
"""
Answer:
{0: 1, 2: 27, 3: 5, 4: 22, 6: 17, 7: 10, 8: 25, 9: 29, 11: 28, 12: 18, 13: 21, 14: 26, 15: 16, 19: 20, 23: 24}
"""

n = 4

numbers = numbersUpToTwice(n)
doubleFactorials = doubleFactorialsOfTwice(n)
#print(doubleFactorials)
maximum = doubleFactorialOfTwice(n)
#print(numbers)    
#print(doubleFactorialsOfTwice(n))   
#print(digits)    
i = 0
while i < maximum:
    digits = digitsOfCode(i, numbers, doubleFactorials) 
    print(i, digits2Pairs(digits, numbers))
    i += 1
