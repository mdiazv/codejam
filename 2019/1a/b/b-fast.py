from functools import reduce
import sys

Ps = [17, 13, 11, 7, 5, 4, 3]

def inv(a, m): 
    a = a % m; 
    for x in range(1, m): 
        if (a * x) % m == 1: 
            return x 

def chinese_remainder(E):
    Rs, Ms = zip(*E)
    N = reduce(lambda a, b: a*b, Ms)
    P = [N // m for m in Ms]
    I = [inv(p, m) for p, m in zip(P, Ms)]
    return sum(r * i * p for r, i, p in zip(Rs, I, P)) % N

T, N, M = map(int, input().split())
for x in range(1, T+1):
    data = []
    for p in Ps:
        print (' '.join(map(str, [p] * 18)))
        f = list(map(int, input().split()))
        data.append( (sum(f) % p, p) )

    print(chinese_remainder(data))
    if input() != '1':
        break
