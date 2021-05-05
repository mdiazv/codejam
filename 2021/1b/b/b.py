from collections import Counter

def highest(N, A, B, U):
    def possible(s):
        have = Counter({s: 1})
        owe = Counter(dict(enumerate(U)))
        while s >= 0:
            extra = have[s] - owe[s] 
            if extra < 0:
                return False
            have[s-A] += extra
            have[s-B] += extra
            s -= 1
        return True

    for s in range(N, 500):
        if possible(s):
            return s+1
    return "IMPOSSIBLE"

T = int(input())
for x in range(1, T+1):
    N, A, B = map(int, input().split())
    U = list(map(int, input().split()))
    h = highest(N, A, B, U)
    print (f"Case #{x}: {h}")
