ITER = 1000000

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

chain = {1: 0}
maximumIndex = 1
maximumLength = 1

i = 1
while i < ITER:
    i += 1
    if i in chain:
        continue
    c = []
    j = i
    while j not in chain:
        c.append(j)
        j = collatz(j)
    assert(j in chain)

    length = len(c) + chain[j]
    if maximumLength < length:
        maximumIndex = i
        maximumLength = length

    while len(c) > 0:
        chain[c[0]] = length
        c.pop(0)
        length -= 1;

print(maximumIndex)
