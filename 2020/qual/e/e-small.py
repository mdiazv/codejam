import sys
sys.setrecursionlimit(100000)

def min_perm(N, K):
    P = [1] * N
    need = K - N
    i = 0
    while i < N and need > 0:
        P[i] = min(need+1, N)
        need = need + 1 - P[i]
        i += 1
    return list(reversed(P))

def assign(P, N, i, j, v):
    P[i, j] = frozenset([v])
    nbs = [(i, k) for k in range(N) if k != j] + [(k, j) for k in range(N) if k != i]
    if all(eliminate(P, N, i, j, v) for i, j in nbs):
        return P
    return False

def eliminate(P, N, i, j, v):
    if v not in P[i, j]:
        return P # already eliminated
    P[i, j] = P[i, j] - {v}
    if not P[i, j]:
        return False # out of options
    if len(P[i, j]) == 1:
        w = next(iter(P[i, j]))
        if not assign(P, N, i, j, w):
            return False
    return P

def search(P, N):
    if P is False:
        return False
    if all(len(vs) == 1 for _, vs in P.items()):
        return P # win
    try:
        n, i, j = min((len(P[i, j]), i, j) for i in range(N) for j in range(N) if len(P[i, j]) > 1)
    except ValueError:
        return False
    return some(search(assign(P.copy(), N, i, j, v), N) for v in P[i, j])

def some(seq):
    for e in seq:
        if e:
            return e
    return False

def fill(M, N):
    P = {(i, j): frozenset(range(1, N+1)) for i in range(N) for j in range(N)}
    for i in range(N):
        for j in range(N):
            if M[i][j] != 0:
                assign(P, N, i, j, M[i][j])
    R = search(P, N)
    if R:
        for i, j in R:
            M[i][j] = next(iter(R[i, j]))
        return M

def solve_p(N, p):
    M = [[0] * N for _ in range(N)]
    for i in range(N):
        M[i][i] = p[i]
    return fill(M, N)

def solve(N, K):
    mp = min_perm(N, K)
    sol = solve_p(N, mp)
    if sol:
        return sol

    S = set(mp)
    if len(S) == 2:
        m = max(S)
        i = mp.index(m)
        mp[i-1] += 1
        mp[i] -= 1

        return solve_p(N, mp)



T = int(input())
for x in range(1, T+1):
    N, K = map(int, input().split())
    M = solve(N, K)
    if M:
        print('Case #{}: POSSIBLE'.format(x))
        for row in M:
            print(' '.join(map(str, row)))
    else:
        print('Case #{}: IMPOSSIBLE'.format(x))
