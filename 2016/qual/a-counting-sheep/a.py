

def solve(N):
    if N == 0:
        return 'INSOMNIA'
    d = set(list(map(str, xrange(10))))
    r = 0
    while d:
        r += N
        d = d - set(list(str(r)))

    return r


T = int(raw_input())
for c in xrange(1, T+1):
    N = int(raw_input())
    print 'Case #{}: {}'.format(c, solve(N))
