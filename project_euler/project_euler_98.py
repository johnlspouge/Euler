#!/usr/bin/python

from collections import Counter 
from itertools import permutations
import math
from string import digits

def index(word):
    return ''.join(sorted(word))

assert(index('BBACC') == 'ABBCC')

def isSquare(n):
    m = int(math.sqrt(n))
    return m * m == n or (m + 1) * (m + 1) == n

assert(not isSquare(48))
assert(isSquare(49))
assert(not isSquare(50))

def toNumber(letters, letter2Number):
    ds = []
    for i in range(0, len(letters)):
        ds.append(letter2Number[letters[i]])
    word = ''.join(ds)
    return int(word)

assert(toNumber('ABC', {'A':'0','B':'1','C':'2'}) == 12)
assert(toNumber('ABC', {'A':'1','B':'1','C':'2'}) == 112)

def isLeading0(word, letter2Number):
    return letter2Number[word[0]] == '0'

assert(isLeading0('ABC', {'A':'0','B':'1','C':'2'}))
assert(not isLeading0('ABC', {'A':'1','B':'1','C':'2'}))

# main        

with open('Data/p042_words.txt', 'r') as content_file:
    content = content_file.read()

words = [x.strip().replace('"','') for x in content.split(',')]
indexes = [index(word) for word in words]
counts = Counter(indexes)

dict = {}
for word in words:
    key = index(word)
    if counts[key] == 1:
        continue
    if key in dict:
        dict[key].append(word)
    else:
        dict[key] = [word]

print(dict.keys())

max = 0

for key in dict.keys():
    words = dict[key]
    letters = list(set(words[0]))
    length = len(letters)
    for p in permutations(digits, length):
        letter2Number = {}
        for i in range(0, length):
            letter2Number[letters[i]] = p[i]
        isSquares = [(letter2Number[word[0]] != '0' and isSquare(toNumber(word, letter2Number))) for word in words]
        count = Counter(isSquares)
        if count[True] > 1:
            for j in range(0, len(words)):
                number = toNumber(words[j], letter2Number)
                if isSquares[j] and max < number:
                    max = number
                    
print(max)
