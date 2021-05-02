from functools import reduce
import operator

def prod(S):
    return reduce(operator.mul, S, 1)

def solve(Deck):
    N = len(Deck)
    DP = {}
    def dp(s, p):
        P, S = prod(p), sum(s)
        if P > S:
            return 0
        if P == S:
            return P
        T = tuple(sorted(p))
        if T in DP:
            return DP[T]
        best = 0
        for k in range(len(s)):
            r = dp(s[:k]+s[k+1:], p+[s[k]])
            best = max(best, r)
        DP[T] = best
        return best
    r = dp(Deck, [])
    return r

T = int(input())
for x in range(1, T+1):
    M = int(input())
    Ps = dict(map(int, input().split()) for _ in range(M))
    Deck = []
    for p, n in Ps.items():
        Deck += [p] * n
    print (f"Case #{x}: {solve(Deck)}")
