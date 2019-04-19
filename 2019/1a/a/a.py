import sys
sys.setrecursionlimit(200000)

def can_jump(a, b):
    if not a:
        return True
    ai, aj = a
    bi, bj = b
    return (ai != bi and aj != bj
        and ai - aj != bi - bj
        and ai + aj != bi + bj)

def search(R, C):
    N = R*C
    def dfs(s, visited, pending):
        if not pending:
            return visited
        for n in [p for p in pending if can_jump(s, p)]:
            pending.remove(n)
            sol = dfs(n, visited + [n], pending)
            pending.add(n)
            if sol and len(sol) == N:
                return sol

    P = {(a, b) for a in range(1, R+1) for b in range(1, C+1)}
    return dfs(None, [], P)

def solve(R, C):
    for a, b in [(a, b) for a in range(1, R+1) for b in range(1, C+1)]:
        sol = search(R, C)
        if sol:
            return sol

T = int(input())
for x in range(1, T+1):
    R, C = map(int, input().split())
    sol = solve(R, C)
    if sol:
        print ('Case #{}: {}'.format(x, 'POSSIBLE'))
        for a, b in sol:
            print(a, b)
    else:
        print ('Case #{}: {}'.format(x, 'IMPOSSIBLE'))
