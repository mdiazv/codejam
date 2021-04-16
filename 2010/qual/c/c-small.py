
def solve(R, K, N, Gs):
    i, euro = 0, 0
    for _ in range(R):
        avail, steps = K, 0
        while avail - Gs[i] >= 0 and steps < N:
            euro += Gs[i]
            steps += 1
            avail, i = avail - Gs[i], (i+1) % N
    return euro

T = int(input())
for x in range(1, T+1):
    R, K, N = map(int, input().split())
    Gs = list(map(int, input().split()))
    print (f"Case #{x}: {solve(R, K, N, Gs)}")
