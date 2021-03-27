import math

def cost(X, Y, S):
    c = 0
    for t in zip(S, S[1:]):
        if t == ('C', 'J'):
            c += X
        if t == ('J', 'C'):
            c += Y
    return c

def paint(X, Y, S):
    s, e, N = 0, 0, len(S)
    fills = [list(f)*N for f in ['C', 'CJ', 'JC', 'JJ']]
    while s < len(S):
        while e < len(S) and S[e] != '?':
            e += 1
        s = e
        while e < len(S) and S[e] == '?':
            e += 1
        # S[s:e] == '?..?'
        n = (e-s) // 2 + 1
        options = [fill[:e-s] for fill in fills]
        pfx = S[s-1] if s > 0 else '?'
        sfx = S[e] if e < len(S) else '?'
        costs = [(cost(X, Y, [pfx] + op + [sfx]), op) for op in options]
        _, best = min(costs)
        S = S[:s] + best + S[e:]
    return cost(X, Y, S)

T = int(input())
for x in range(1, T+1):
    X, Y, S = input().split()
    print (f"Case #{x}: {paint(int(X), int(Y), list(S))}")
