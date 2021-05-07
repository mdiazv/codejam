#!/usr/bin/python
from decimal import *

def solve(n):
    five = Decimal(5)
    getcontext().prec = 100
    return (3 + five.sqrt()) ** (n if n < 103 else (n - 3) % 100 + 3)

T = int(raw_input())
for x in range(1, T+1):
    N = int(raw_input())
    print "Case #{0}: {1:03d}".format(x, int(solve(N) % 1000)) 
