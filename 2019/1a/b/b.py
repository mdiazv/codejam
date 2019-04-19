from functools import reduce
import sys

Ps = [17, 13, 11, 7, 5, 4, 3]

def chinese_remainder_slow(M, E):
    for i in range(0, M+1):
        s = [(i % p, p) for p in Ps]
        if s == E:
            return i

T, N, M = map(int, input().split())
for x in range(1, T+1):
    data = []
    for p in Ps:
        print (' '.join(map(str, [p] * 18)))
        f = list(map(int, input().split()))
        data.append( (sum(f) % p, p) )

    print(chinese_remainder_slow(M, data))
    if input() != '1':
        break
