
def solve(S):
    values = [1, 0] + list(range(2, 64))
    tr, k = {}, 0
    for c in S:
        if c not in tr:
            tr[c] = values[k]
            k += 1
    t, p = 0, 0
    base = max(2, len(tr))
    for c in reversed(S):
        t += tr[c] * (base ** p)
        p += 1
    return t

T = int(input())
for x in range(1, T+1):
    S = list(input())
    print ("Case #{}: {}".format(x, solve(S)))
