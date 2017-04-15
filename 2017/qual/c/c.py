

def leap(stalls, k):
    M = max(stalls)
    skip = min(stalls[M], k)
    stalls[M] -= skip
    if stalls[M] == 0:
        del stalls[M]

    M -= 1
    h = M / 2
    H = M - h
    if h not in stalls:
        stalls[h] = 0
    if H not in stalls:
        stalls[H] = 0
    stalls[h] += skip
    stalls[H] += skip

    return stalls, h, H, k - skip


T = int(raw_input())
for x in xrange(1, T+1):
    N, K = map(int, raw_input().split())
    stalls = {N: 1}
    while K:
        stalls, m, M, K  = leap(stalls, K)
    print "Case #{}: {} {}".format(x, M, m)
