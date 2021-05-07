import heapq as H

def minutes(s):
    h, m = map(int, s.split(':'))
    return h*60+m

def parse(both):
    return tuple(map(minutes, both.split()))

def sim(T, TA, TB):
    E = []
    FN = {
        0: lambda a, b: (a, b+1),
        1: lambda a, b: (a+1, b),
        2: lambda a, b: (a-1, b),
        3: lambda a, b: (a, b-1),
    }
    for s, e in TA:
        H.heappush(E, (s, 2))
        H.heappush(E, (e+T, 0))
    for s, e in TB:
        H.heappush(E, (s, 3))
        H.heappush(E, (e+T, 1))
    
    sa, sb = 0, 0
    a, b = 0, 0
    while E:
        t, fn = H.heappop(E)
        a, b = FN[fn](a, b)
        if a < 0:
            a = 0
            sa += 1
        if b < 0:
            b = 0
            sb += 1
    return sa, sb

N = int(input())
for x in range(1, N+1):
    T = int(input())
    NA, NB = map(int, input().split())
    TA = sorted(parse(input()) for _ in range(NA))
    TB = sorted([parse(input()) for _ in range(NB)])
    a, b = sim(T, TA, TB)
    print (f"Case #{x}: {a} {b}")
