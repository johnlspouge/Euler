#!/usr/bin/python

s = \
    "75 " \
    "95 64 " \
    "17 47 82 " \
    "18 35 87 10 " \
    "20 04 82 47 65 " \
    "19 01 23 75 03 34 " \
    "88 02 77 73 07 63 67 " \
    "99 65 04 28 06 16 70 92 " \
    "41 41 26 56 83 40 80 70 33 " \
    "41 48 72 33 47 32 37 16 94 29 " \
    "53 71 44 65 25 43 91 52 97 51 14 " \
    "70 11 33 28 77 73 17 78 39 68 17 57 " \
    "91 71 52 38 17 14 91 43 58 50 27 29 48 " \
    "63 66 04 68 89 53 67 30 73 16 69 87 40 31 " \
    "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

numbers = s.split(" ")
rows = []
j = 0
index = 0
while index < len(numbers):
    j += 1
    list = []
    i = 0
    while i < j and index < len(numbers):
        list.append(int(numbers[index]))
        index += 1
        i += 1
    rows.append(list)

# print(rows)

m = [rows[0][0]]
row = 1
while row < len(rows):
    e0 = rows[row][0] + m[0]
    e1 = rows[row][len(rows[row]) - 1] + m[len(rows[row]) - 2]
    col = 1
    while col < len(rows[row]) - 1:
        m[col - 1] = rows[row][col] + max(m[col - 1], m[col])
        col += 1
    m.insert(0, e0)
    m[-1] = e1
    row += 1
#    print(m)

print(max(m))