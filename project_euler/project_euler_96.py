#!/usr/bin/python

debug = False

from enum import Enum
from copy import deepcopy
import time

class SolutionStatus(Enum):
    SOLVED = 0
    UNDETERMINED = 1
    CONTRADICTORY = 2

digitSet = {'1','2','3','4','5','6','7','8','9'}
   
def matrixToString(rows):
    return "\n".join(map("".join, rows))

def stringToMatrix(sudoku):
    rows = []
    for line in sudoku.split("\n"):
        rows.append(list(line))
    return rows

def possibleSet(rows,i,j):
    if rows[i][j] != '0':
        raise Exception('({},{}) was already filled with {}.'.format(i,j,rows[i][j])) # no need to solve
    digits = []
    for k in range(0,9):
        digits.append(rows[i][k]) # rows
        digits.append(rows[k][j]) # cols
    M = (i // 3) * 3
    N = (j // 3) * 3
    for m in range(M,M+3):
        for n in range(N,N+3):
            digits.append(rows[m][n]) # 3x3 square
    impossibleSet = set(digits)
    return digitSet.difference(impossibleSet)

def solveGrid(rows, smallestDigitSet):
    isSolved = False
    isChanged = True
    while not isSolved and isChanged:
        isSolved = True
        isChanged = False
        for i in range(0,9):
            for j in range(0,9):
                if rows[i][j] != '0':
                    continue
                isSolved = False
                digitSet = possibleSet(rows,i,j)
                if len(digitSet) == 0:
                    return SolutionStatus.CONTRADICTORY
                elif len(digitSet) == 1:
                    rows[i][j] = digitSet.pop()
                    isChanged = True
                else:
                    if debug:
                        print(digitSet)
                        print(smallestDigitSet)
                    if len(smallestDigitSet.keys()) == 0 or len(digitSet) < len(smallestDigitSet['digitSet']):
                        smallestDigitSet['coordinates'] = [i, j]
                        smallestDigitSet['digitSet'] = digitSet
        if not isSolved and not isChanged:
            return SolutionStatus.UNDETERMINED
    return SolutionStatus.SOLVED

def solveGridWithTries(rows0):
    rows = deepcopy(rows0)
    tries = [rows]
    while True:
        smallestDigitSet = {}
        rows = tries.pop()
        solutionStatus = solveGrid(rows, smallestDigitSet)
        if solutionStatus == SolutionStatus.SOLVED:
            return rows
        elif solutionStatus == SolutionStatus.UNDETERMINED:
            for digit in list(smallestDigitSet['digitSet']):
                rows = deepcopy(rows)
                coordinates = smallestDigitSet['coordinates']
                rows[coordinates[0]][coordinates[1]] = digit 
                tries.append(rows)
        elif solutionStatus == SolutionStatus.CONTRADICTORY:
            assert(len(tries) != 0)

# https://www.geeksforgeeks.org/program-sudoku-generator/

sudokuGeek = \
"""\
230415068
080236519
160987234
317094025
458120697
926058301
000500102
000842903
592371486\
"""    

solvedGeek = \
"""\
239415768
784236519
165987234
317694825
458123697
926758341
843569172
671842953
592371486\
"""  

assert(matrixToString(solveGridWithTries(stringToMatrix(sudokuGeek))) == solvedGeek)
 
# Grid 1 from the file

sudoku1 = \
"""\
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300\
"""    

solved1 = \
"""\
483921657
967345821
251876493
548132976
729564138
136798245
372689514
814253769
695417382\
"""  

rows = stringToMatrix(sudoku1)
assert(possibleSet(rows,0,0) == {'4', '5'})
smallestDigitSet = {}
assert(solveGrid(rows, smallestDigitSet) == SolutionStatus.SOLVED)
assert(matrixToString(rows) == solved1)
rows = stringToMatrix(sudoku1)
assert(matrixToString(solveGridWithTries(rows)) == solved1)

# Grid 8 from the file

sudoku8 = \
"""\
200080300
060070084
030560209
000105408
000000000
402706000
301007040
720040060
004010003\
"""    

solved8 = \
"""\
245981376
169273584
837564219
976125438
513498627
482736951
391657842
728349165
654812793\
"""  

rows = stringToMatrix(sudoku8)
assert(possibleSet(rows,4,2) == {'9', '6', '8', '7', '5', '3'})
#debug = True
smallestDigitSet = {}
assert(len(smallestDigitSet.keys()) == 0)
assert(solveGrid(rows, smallestDigitSet) == SolutionStatus.UNDETERMINED)
assert(smallestDigitSet == {'coordinates': [0, 3], 'digitSet': {'4', '9'}})
assert(matrixToString(rows) == sudoku8)

rows = stringToMatrix(sudoku8)
assert(matrixToString(solveGridWithTries(rows)) == solved8)

# Main


with open('Data/p096_sudoku.txt', 'r') as content_file:
    content = content_file.read()

lines = [x for x in content.split("\n")]

start = time.time()
puzzleNumber = 0
sum = 0
while len(lines) != 0:
    puzzleNumber += 1
    lines.pop(0)
    rows0 = []
    for i in range(0,9):
        assert(len(lines) != 0)
        rows0.append(list(lines.pop(0)))
    rows = solveGridWithTries(rows0)
    upperLeft = [rows[0][0], rows[0][1], rows[0][2]]
    number = int(''.join(upperLeft))
    sum += number

end = time.time()
print( end - start ) 
print(sum)
    
                    
    # Solves the puzzle    
 #   print(rows[0])
