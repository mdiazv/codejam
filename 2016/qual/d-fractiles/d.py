
dp = [[[0] * 101 for _ in xrange(101)] for _ in xrange(101)]

for c in xrange(1, 101):
    for r in xrange(100):
        m = 1
        for k in xrange(c+r, 101):
            dp[c][r][k] = (dp[c-1][r][k]+1) * k - m
            m += 1

T = int(raw_input())
for x in xrange(1, T+1):
    K, C, S = map(int, raw_input().split())
    R = []
    r = 0
    print "Case #{}:".format(x),
    for _ in xrange(S):
        take = min(C, K-r)
        R.append(dp[take][r][K] + 1)
        r += take
        if r == K:
            for p in R:
                print " {}".format(p),
            print
            break
    if r != K:
        print " IMPOSSIBLE"

