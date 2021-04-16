
def solve(R, K, N, Gs):
    def step(i):
        start_i, steps, euro = i, 0, 0
        while euro + Gs[i] <= K and steps < N:
            euro += Gs[i]
            steps += 1
            i = (i+1) % N
        return euro, i

    seen_at = {}
    i, r, euro = 0, 0, 0
    while r < R:
        seen_at[i] = (r, euro)
        s_euro, i = step(i)
        euro += s_euro
        r += 1
        # Modular simplification upon finding first loop
        if i in seen_at:
            c_start, c_start_euro = seen_at[i]
            c_len = r - c_start
            c_euro = euro - c_start_euro
            # speed up
            R -= c_start
            times = R // c_len
            R %= c_len
            euro = c_start_euro + c_euro * times
            seen_at = {}
            r = 0

    return euro

T = int(input())
for x in range(1, T+1):
    R, K, N = map(int, input().split())
    Gs = list(map(int, input().split()))
    print (f"Case #{x}: {solve(R, K, N, Gs)}")
