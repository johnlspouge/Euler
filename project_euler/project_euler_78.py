#!/usr/bin/python

def pentagonal(k):
    return k * (3 * k - 1) // 2

def partition(ps,n,mod): # m = modulus
    p = 0
    k = 1
    while True:
        m = n - pentagonal(k)
        if m < 0:
            break;
        term = ps[m]
        if k % 2 == 0:
            term = -term
        p += term
        if mod != 0:
            p = p % mod
        k += 1
    k = -1
    while True:
        m = n - pentagonal(k)
        if m < 0:
            break;
        term = ps[m]
        if k % 2 == 0:
            term = -term
        p += term
        if mod != 0:
            p = p % mod
        k -= 1
    return p

def partitions(n,mod = 0): # m = modulus
    ps = [1]
    for k in range(1,n+1):
        p = partition(ps,k,mod)
        ps.append(p)
    return ps

# Tests

ps = partitions(10)
ps0 = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42] 
assert(ps == ps0)

ps = partitions(10,10)
ps0 = [1, 1, 2, 3, 5, 7, 1, 5, 2, 0, 2]      
assert(ps == ps0)

# Main

MOD = 1000000

ps = [1]
k = 1
while True:
        p = partition(ps,k,MOD)
        ps.append(p)
        if p == 0:
            break
        k += 1

print(k)

