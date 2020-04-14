def rindex(R, c):
    for i in range(len(R)-1, -1, -1):
        if R[i] == c:
            return i
    return -1

def solve(N, Ws):
    W = sorted([(sum(c == '*' for c in w), w, w.split("*")) for w in Ws])
    R = [''] * 10000
    for s, w, p in W:
        n = len(p)
        if n == 1:
            # single word
            combined = ''.join(R)
            if w == combined:
                R = list(w)
                continue
            else:
                return '*'
        for i, c in enumerate(p[0]):
            if R[i] == '':
                R[i] = c
            elif R[i] != c:
                return '*'

        for i, c in enumerate(reversed(p[-1])):
            if R[-i-1] == '':
                R[-i-1] = c
            elif R[-i-1] != c:
                return '*'

    plen = R.index('')
    slen = rindex(R, '')
    S = ''.join(R[:plen])

    for s, w, ps in W:
        for p in ps[1:-1]:
            S += p

    S += ''.join(R[slen:])
    return S

T = int(input())
for x in range(1, T+1):
    N = int(input())
    Ws = [input() for _ in range(N)]
    w = solve(N, Ws)
    print("Case #{}: {}".format(x, w))
