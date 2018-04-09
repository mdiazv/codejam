from collections import defaultdict
from itertools import groupby

def new_count(P, G):
    s = c = 0
    for g in G:
        if s % P == 0:
            c += 1
        s = (s+g) % P
    return c

def best_order(N, P, G):
    keyfn = lambda x: x % P
    M = defaultdict(list)
    for g in groupby(sorted(G, key=keyfn), key=keyfn):
        head, group = g
        M[head] = list(group)

    R = M[0]
    if P < 4:
        N = min(len(M[1]), len(M[2]))
        R += [val for pair in zip(M[1], M[2]) for val in pair]
        R += M[1][N:]
        R += M[2][N:]

    else:
        N = len(M[2]) // 2
        R += M[2][:2*N]
        mod = M[2][2*N:]

        N = min(len(M[1]), len(M[3]))
        R += [val for pair in zip(M[1], M[3]) for val in pair]

        R += mod
        R += M[1][N:]
        R += M[3][N:]

    return new_count(P, R)

T = int(input())
for x in range(1, T+1):
    N, P = map(int, input().split())
    G = map(int, input().split())
    print ('Case #{}: {}'.format(x, best_order(N, P, G)))
