
def solve(M, Ps, Deck):
    N = len(Deck)
    DP = {}
    def dp(k, s, p):
        if k == N:
            return s if s == p else 0
        if (k, s, p) in DP:
            return DP[k, s, p]
        in_sum = dp(k+1, s+Deck[k], p)
        in_prod = dp(k+1, s, p*Deck[k])
        DP[k, s, p] = max(in_sum, in_prod)
        return DP[k, s, p]
    r = dp(0, 0, 1)
    return r


T = int(input())
for x in range(1, T+1):
    M = int(input())
    Ps = dict(map(int, input().split()) for _ in range(M))
    Deck = []
    for p, n in Ps.items():
        Deck += [p] * n
    print (f"Case #{x}: {solve(M, Ps, Deck)}")
