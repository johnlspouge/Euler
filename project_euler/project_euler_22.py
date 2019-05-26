#!/usr/bin/python

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter2Score = {}
i = 0
while i < len(letters):
    letter2Score[letters[i]] = i + 1
    i += 1

def score(name):
    sum = 0
    for a in name:
        #print(a)
        sum += letter2Score[a]

    return sum

fh = open("Data/names.txt", "r")
s = fh.read()
names = s.split(",")
names.sort()

#print(names[0])
#print(len(names))

sum = 0
i = 0
while i != len(names):
    name = names[i].replace('"', '')
    #if i == 937:
        #print(name)
        #print(score(name))
    sum += (i + 1) * score(name)
    i += 1

print(sum)