import sys
sys.setrecursionlimit(100000)

def revstep(P, k):
    return [x+1 for x in list(reversed(P[:k])) + [0] + P[k:]]

def engsort(N, C):
    def search(n, c, P):
        if n == N and c == C:
            return P
        if n > N or c > C:
            return None
        base = n if C - c > N else 0
        for k in range(base, n+1):
            p = revstep(P, k)
            s = search(n+1, c+k+1, p)
            if s:
                return s

    if C < N-1 or C > N*(N+1)//2 + 1:
        return None
    return search(1, 0, [1])

T = int(input())
for x in range(1, T+1):
    N, C = map(int, input().split())
    perm = engsort(N, C)
    print (f"Case #{x}: {' '.join(map(str, perm)) if perm else 'IMPOSSIBLE'}")
