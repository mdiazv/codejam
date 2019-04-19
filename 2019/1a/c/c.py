from collections import Counter

def largest(N, W):
    s = 0
    C = Counter(w[k:] for w in W for k in range(len(w)))
    for p in sorted(C, key=lambda w: -len(w)):
        if C[p] >= 2:
            s += 2
            for k in range(1, len(p)):
                C[p[k:]] -= 2
    return s

T = int(input())
for x in range(1, T+1):
    N = int(input())
    W = [input() for _ in range(N)]
    print ('Case #{}: {}'.format(x, largest(N, W)))
