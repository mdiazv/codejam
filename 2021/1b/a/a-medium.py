from itertools import permutations
import sys

M = 360 * 12 * 10 **10

def time2ang(h, m, s):
    ns = (M // 12) * h + (M // 60) * m // 12 + (M // 60) * s // 720
    ns %= M
    return ns, (ns * 12) % M, (ns * 720) % M


def tell_time(A, B, C):
    Hs = [A, B, C]
    for th, tm, ts in permutations([A, B, C]):
        print (th, tm, ts)
        ns = th
        dt = [(th-tm+M) % M, (th-ts+M) % M]
        dm = ns * 12
        ds = ns * 720
        du = [(th-dm+M) % M, (th-ds+M) % M]
        print (dt, du)

        h = th % (M // 12)
        m = tm % (M // 60)
        s = ts % (M // 60)

        for gh in range(12):
            for gm in range(60):
                for gs in range(60):
                    gth, gtm, gts = time2ang(gh, gm, gs)
                    if (gth, gtm, gts) == (th, tm, ts):
                        print ("found time", gh, gm, gs)
                        return gh, gm, gs, 0

    return 0, 0, 0, 0

T = int(input())
for x in range(1, T+1):
    A, B, C = map(int, input().split())
    h, m, s, n = tell_time(A, B, C)
    print (f"Case #{x}: {h} {m} {s} {n}")
