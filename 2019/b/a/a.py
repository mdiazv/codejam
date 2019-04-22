from collections import Counter

class Freq:
    def __init__(self, W):
        C = Counter()
        Cs = []
        for c in W:
            Cs.append(C.copy())
            C[c] += 1
        Cs.append(C)
        self.Cs = Cs
    def palin(self, a, b):
        Ca = self.Cs[a-1]
        Cb = self.Cs[b]
        C = Cb.copy()
        C.subtract(Ca)
        odd = 0
        for e in C:
            if C[e] % 2 != 0:
                odd += 1
            if odd > 1:
                break
        return odd <= 1

T = int(input())
for x in range(1, T+1):
    N, Q = map(int, input().split())
    F = Freq(input())
    R = 0
    for _ in range(Q):
        a, b = map(int, input().split())
        if F.palin(a, b):
            R += 1
    print("Case #{}: {}".format(x, R))
