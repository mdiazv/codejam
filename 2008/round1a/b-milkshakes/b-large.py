#!/usr/bin/python
import sys

def happy(i):
    for f, m in cust[i]:
        if malts[f] == m:
            return True
    return False

def solve():
    for i in range(M):
        if likesm[i] == 0 and not happy(i):
            return False
        if not happy(i):
            malts[likesm[i]] = 1
            return solve()
    return True
            
T = int(raw_input())
for x in range(1, T+1):
    N = int(raw_input())
    M = int(raw_input())
    cust = []
    likesm = [0]*M
    malts = [0]*(N+1)
    for i in range(M):
        C = []
        c = map(int, raw_input().split())
        for m in range(1, c[0]*2+1, 2):
            C.append((c[m], c[m+1]))
            if c[m+1] == 1:
                likesm[i] = c[m]
        cust.append(C)
    if solve():
        print "Case #{0}: {1}".format(x, ' '.join(map(str, malts[1:])))
    else:
        print "Case #{0}: IMPOSSIBLE".format(x)
