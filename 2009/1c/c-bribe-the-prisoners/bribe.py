from functools import lru_cache

def solve(P, Q, Qs):
    @lru_cache(maxsize=P*P)
    def dp(l, u):
        if u-l < 2:
            return 0
        opts = [u-l-1 + dp(l, k) + dp(k+1, u) for k in Qs if l <= k and k < u]
        return min(opts) if opts else 0
    return dp(1, P+1)


T = int(input())
for x in range(1, T+1):
    P, Q = map(int, input().split())
    Qs = list(map(int, input().split()))
    print ("Case #{}: {}".format(x, solve(P, Q, Qs)))
