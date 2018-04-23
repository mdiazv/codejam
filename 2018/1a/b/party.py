from itertools import islice

class Cashier:
    def __init__(self, m ,s, p):
        self.m = m
        self.s = s
        self.p = p
    def cap(self, t):
        raw = max(0, (t - self.p) // self.s)
        return min(self.m, raw)
    def maxt(self):
        return self.m * self.s + self.p

def solve(R, B, Cs):
    def simulate(t):
        cs = reversed(sorted(c.cap(t) for c in Cs))
        return sum(islice(cs, R))
    def findT(tmin, tmax):
        if tmin+1 == tmax:
            return tmax
        t = (tmin + tmax) // 2
        n = simulate(t)
        if n < B:
            return findT(t, tmax)
        return findT(tmin, t)
        
    tmax = 1 + max(map(Cashier.maxt, Cs))
    return findT(0, tmax)

T = int(input())
for x in range(1, T+1):
    R, B, C = map(int, input().split())
    Cs = [None] * C
    for i in range(C):
        m, s, p = map(int, input().split())
        Cs[i] = Cashier(m, s, p)
    print ('Case #{}: {}'.format(x, solve(R, B, Cs)))
