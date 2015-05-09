#!/usr/bin/python
import sys
sys.setrecursionlimit(10000)

def we_happy(shop):
    for i in range(1, M+1):
        happy = 0
        for j in range(1, N+1):
            if shop[i][j] == shop[0][j]:
                happy = 1
                break
        if happy != 1:
            return 0
    return 1

def what_kind(shop, flav):
    kind = -1
    for i in range(1, M+1):
        if shop[i][flav] != -1:
            if kind == -1:
                kind = shop[i][flav]
            elif kind != -1 and kind != shop[i][flav]:
                return -1
    if kind == -1:
        return 0
    return kind

def malted(shop):
    m = 0
    for j in range(1, N+1):
        if shop[0][j] == 1:
            m = m + 1
    return m

def solve(shop, flav):
    if flav == N+1:
        if we_happy(shop):
            return malted(shop)
        return -1

    kind = what_kind(shop, flav)
    if kind != 0:
        shop[0][flav] = 0
        a = solve(shop, flav+1)
        sa = shop[0][:]
        shop[0][flav] = 1
        b = solve(shop, flav+1)
        sb = shop[0][:]
        if a == -1:
            if b == -1:
                return -1
            shop[0] = sb
            return b
        else:
            if b == -1:
                shop[0] = sa
                return a
            if a < b:
                shop[0] = sa
                return a
            shop[0] = sb
            return b

    shop[0][flav] = 0
    return solve(shop, flav+1)
    
T = int(raw_input())
for x in range(1, T+1):
    N = int(raw_input())
    M = int(raw_input())
    malts = [0]*N
    happy = [0]*M
    shop = [[-1]*(N+1) for i in range(M+1)]
    for i in range(1, M+1):
        shop[i][0] = 0
        c = map(int, raw_input().split())
        for m in range(1, c[0]*2+1, 2):
            shop[i][c[m]] = c[m+1]
    for j in range(N+1):
        shop[0][j] = 0

    r = solve(shop, 1)
    if r == -1:
        print "Case #{0}: IMPOSSIBLE".format(x)
        print >> sys.stderr, "Case #{0}: IMPOSSIBLE".format(x)
    else:
        print "Case #{0}: {1}".format(x, ' '.join(map(str, shop[0][1:])))
        print >> sys.stderr, "Case #{0}: {1}".format(x, ' '.join(map(str, shop[0][1:])))

