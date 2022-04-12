
def solve(Ps):
    Ms = [min(Ps[i][j] for i in range(3)) for j in range(4)]
    if sum(Ms) < 10 ** 6:
        return None
    k = 0
    r = [0, 0, 0, 0]
    for i in range(4):
        add = min((10 ** 6) - k, Ms[i])
        r[i] = add
        k += add
    return r

T = int(input())
for x in range(1, T+1):
    Ps = [list(map(int, input().split())) for _ in range(3)]
    r = solve(Ps)
    print (f'Case #{x}: {"IMPOSSIBLE" if not r else " ".join(map(str, r))}')
