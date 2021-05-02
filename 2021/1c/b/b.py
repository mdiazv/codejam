
def roaring(y):
    def ok(l, r):
        if r == "":
            return True
        n = str(int(l)+1)
        if not r.startswith(n):
            return False
        return ok(n, r[len(n):])

    y = str(y)
    return any(ok(y[:k], y[k:]) for k in range(1, len(y)))

def build(pfx, k):
    s = str(pfx)
    for _ in range(1, k):
        s += str(pfx+1)
        pfx += 1
    return int(s)

def next_roaring(Y):
    if Y < 10:
        return 12

    def search(a, b, n):
        if a+1 == b:
            return build(a, n), build(b, n)
        h = (a+b)//2
        ph = build(h, n)
        if ph > Y:
            return search(a, h, n)
        return search(h, b, n)
    
    best = Y * 10 ** 10
    for n in range(20):
        for k in search(1, 10 ** 10, n):
            if roaring(k) and k > Y and k < best:
                best = k

    return best

T = int(input())
for x in range(1, T+1):
    Y = int(input())
    n = next_roaring(Y)
    print (f"Case #{x}: {n}")
