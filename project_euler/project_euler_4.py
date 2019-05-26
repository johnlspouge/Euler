#!/usr/bin/python

# Returns true if n is a palindrome.
def Is_Palindrome(n, base = 10):

    digits = [];
    
    while n > 0:
        digits.append(n % base)
        n //= base

    d = len(digits)
    lefts = digits[:d // 2]
    rights = digits.reverse()
    rights = digits[:d // 2]
    
    while len(lefts) > 0:
        if lefts.pop() != rights.pop():
            return False
            
    return True;


palindrome = 0
m = 100

while m < 1000:
    n = 100
    while n < 1000:
        p = m * n
        if Is_Palindrome(p):
            if m * n > palindrome:
                palindrome = m * n
        n += 1
    m += 1
        
print(palindrome)
