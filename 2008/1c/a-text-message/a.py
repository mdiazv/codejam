#!/usr/bin/python

N = int(raw_input())
for x in range(1, N+1):
    P, K, L = map(int, raw_input().split())
    freq = sorted(map(int, raw_input().split()), reverse=True)
    s = 0
    v = 1
    for k in range(0, L, K):
        s += sum(freq[k:k+K]) * v
        v += 1
    print "Case #{0}: {1}".format(x, s)
