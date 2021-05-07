#!/usr/bin/python

T = int(raw_input())
for case in range(1, T+1):
    N = int(raw_input())
    A = sorted(map(int, raw_input().split()))
    B = sorted(map(int, raw_input().split()), reverse=True)
    print "Case #{0}: {1}".format(case, sum(a*b for a, b in zip(A, B)))
