import sys
sys.setrecursionlimit(100000)

def highest(N, A, B, U):
    have = [0] * N
    def bt(high, have=have):
        if all(h >= u for h, u in zip(have, U)):
            return True
        if any(h < u and high < k for k, (h, u) in enumerate(zip(have, U))):
            return False
        for k in range(len(have)):
            if have[k]:
                a, b = k - A, k - B
                have[k] -= 1
                if a >= 0:
                    have[a] += 1
                if b >= 0:
                    have[b] += 1
                if bt(max(i for i in range(len(have)) if have[i]), have):
                    return True
                have[k] += 1
                if a >= 0:
                    have[a] -= 1
                if b >= 0:
                    have[b] -= 1
        return False

    for s in range(100):
        print (s)
        have = [0] * max(N, s+1)
        have[s] = 1
        if bt(s, have):
            return s+1

    return "IMPOSSIBLE"

T = int(input())
for x in range(1, T+1):
    N, A, B = map(int, input().split())
    U = list(map(int, input().split()))
    h = highest(N, A, B, U)
    print (f"Case #{x}: {h}")
