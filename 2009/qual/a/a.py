import re

L, D, N = map(int, raw_input().split())
Ws = [raw_input() for _ in xrange(D)]
Cs = [raw_input() for _ in xrange(N)]

for x, c in enumerate(Cs):
    c = c.replace('(', '[').replace(')', ']')
    r = sum(1 for w in Ws if re.match(c, w))
    print "Case #{}: {}".format(x+1, r)
