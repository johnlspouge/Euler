#!/usr/bin/python

from math import sqrt
from string import ascii_uppercase

letter2number = {}

for i in range(0, len(ascii_uppercase)):
    letter2number[ascii_uppercase[i]] = i + 1
    
def wordToNumber(word):
    number = 0
    for letter in word:
        if letter not in letter2number.keys():
            print(letter)
            exit(1)
        number += letter2number[letter]
    return number

def isTriangleNumber(number):
    n = int(sqrt(2 * number))
    if n * (n + 1) == 2 * number:
        return True
    return False

def isTriangleWord(word):
    return isTriangleNumber(wordToNumber(word))

assert(letter2number['Z'] == 26)
assert(wordToNumber('SKY') == 55)
assert(isTriangleWord('SKY'))

with open('Data/p042_words.txt', 'r') as content_file:
    content = content_file.read()

words = [x.strip().replace('"','') for x in content.split(',')]

print(sum(1 for word in words if isTriangleWord(word)))
