#!/usr/bin/python

#See https://en.wikipedia.org/wiki/Pell_number#Pythagorean_triples_2

# a == b : not checked because of time
def isRightAngle(x,y,a,b):
    if x == 0 and b == 0:
        return True
    if y == 0 and a == 0:
        return True
    if y == 0 and x == a:
        return True
    if x == 0 and y == b:
        return True
    if x * (a - x) == -(b - y) * y :
        return True
    if a * (a - x) == -(b - y) * b :
        return True
    return False
        
M = 50 # M = 2 # 
sum = 0 
for x in range(0,M+1):
    for y in range(0,M+1):
        if x == 0 and y == 0:
            continue
        for a in range(x,M+1):
            for b in range(0,M+1):
                if a == 0 and b == 0:
                    continue
                if a == x and 0 < b:
                    continue
                if a == x and b == y:
                    continue
                if isRightAngle(x,y,a,b):
                    print(x,y,",",a,b)
                    sum += 1
                    
print(sum)
