ITER = 1000000

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

chain = {1: [1]}

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

    chain[i] = c + chain[j]

    c = chain[i].copy()
    while len(c) > 2 and c[1] != j:
        c.pop(0)
        chain[c[0]]= c.copy()

maximumIndex = 1
maximumLength = 1
for i in range(1, ITER):
    if maximumLength < len(chain[i]):
        maximumIndex = i
        maximumLength = len(chain[i])

print(maximumIndex)
print(len(chain[maximumIndex]))