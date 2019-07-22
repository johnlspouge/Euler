#!/usr/bin/python

import collections

N = 100 

month = [0,3,3,6,1,4,6,2,5,0,3,5]
print(month)
counter = collections.Counter(month)
print(counter)

monthLeapYear = month.copy()
print(monthLeapYear)
i = 0
while i < len(monthLeapYear):
    if 2 <= i: 
        monthLeapYear[i] += 1
    i += 1
counterLeapYear = collections.Counter(month)
print(counterLeapYear)
        
year = 0
remainder = 0

numberSunday = 0

while year < N:
    
    remainder %= 7    
    feb29 = year % 4 == 0 and year > 0

    c = counter
    if feb29:
        c = counterLeapYear
    
    numberSunday += c[6 - remainder]
                
    if feb29:
        remainder += 2
    else:
        remainder += 1
    year += 1

print(numberSunday)