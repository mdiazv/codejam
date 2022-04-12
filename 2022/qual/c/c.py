
def solve(N, Ds):
    k = 1
    for d in Ds:
        if k <= d:
            k += 1
    return k-1

T = int(input())
for x in range(1, T+1):
    N = int(input())
    Ds = list(sorted(map(int, input().split())))
    ways = solve(N, Ds)
    print (f'Case #{x}: {ways}')
