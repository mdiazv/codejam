from itertools import permutations

M = 360 * 12 * 10 **10

def solve(Hs):
    for h, m, s in permutations(Hs):
        diff = m - h
        if diff < 0:
            diff += M
        for k in range(12):
            total = k * M + diff
            if total % 11 != 0:
                continue
            x = total // 11
            shift = h - x
            if shift < 0:
                shift += M

            if h != (x + shift) % M:
                continue
            if m != (12*x + shift) % M:
                continue
            if s != (720*x + shift) % M:
                continue

            ns = x % 10 ** 9
            x //= 10 ** 9
            s = x % 60
            x //= 60
            m = x % 60
            h = x // 60
            if h < 12:
                return h, m, s, ns

T = int(input())
for x in range(1, T+1):
    Hs = list(map(int, input().split()))
    h, m, s, ns = solve(Hs)
    print(f"Case #{x}: {h} {m} {s} {ns}")
