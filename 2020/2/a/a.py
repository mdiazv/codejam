
def cust(gap, fn):
    def search(a, b):
        if a+1 == b:
            return a, fn(a)
        h = (a+b) // 2
        p = fn(h)
        if p > gap:
            return search(a, h)
        return search(h, b)
    cs, ps = search(1, 10 ** 18)
    if ps > gap:
        ps -= cs
        cs -= 1
    return cs, 0 if cs == 0 else ps

def sum_of(k):
    return k*(k+1)//2

def sum_prog(b, n):
    return n * (b + (b + 2*(n-1))) // 2

def solve(L, R):
    gap = abs(L-R)
    cs, ps = cust(gap, sum_of)
    if L >= R:
        L -= ps
    else:
        R -= ps

    if L >= R:
        cl, rl = cust(L, lambda x: sum_prog(cs+1, x))
        cr, rr = cust(R, lambda x: sum_prog(cs+2, x))
    else:
        cr, rr = cust(R, lambda x: sum_prog(cs+1, x))
        cl, rl = cust(L, lambda x: sum_prog(cs+2, x))

    return cs+cl+cr, L-rl, R-rr

T = int(input())
for x in range(1, T+1):
    L, R = map(int, input().split())
    n, l, r = solve(L, R)
    print (f"Case #{x}: {n} {l} {r}")

