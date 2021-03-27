from collections import Counter
from itertools import groupby
from operator import itemgetter
import statistics
import random
import math

def cheater_likelyhood(SR, err):
    Rs = []
    for block_size in [50, 100, 500, 1000, 2000]:
        C = Counter(SR[-block_size:])
        print (C)
        Rs.append(block_size - abs(C['0'] - C['1']))

    Rs.append(sum(x == '1' for x in SR))
    Rs.append(sum(x == '0' for x in SR[-100:]))
    Rs.append(err)
    weights = [250, 100, 10, 10, 5, 1, -20, ]

    Rs.insert(0, sum (r*w for r, w in zip(Rs, weights)))
    return tuple(Rs)

def remap(base, step, Fn):
    return [base + (step*v) for v in Fn]

def f(p, q):
    x = p - q
    return 1 / (1 + math.exp(-x))

def error(actual, expected):
    return sum(a != e for a, e in zip(actual, expected))

def cheater(Rs):
    Qs = [0] * 10000
    ok = []
    for r in Rs:
        k = 0
        for i, v in enumerate(r):
            Qs[i] += v == '0'
            k += v == '1'
        ok.append(k)

    # Remap by skill
    PQs = [q/100 for q in Qs]
    PQRemap = remap(-3.0, 0.06, Qs)
    QDs = sorted([(q, i) for i, q in enumerate(PQRemap)])

    PRemap = remap(-3, 0.0006, ok)
    PDs = sorted([(p, i) for i, p in enumerate(PRemap)])

    # appearance order
    SPs = [p for _, p in sorted([(i, p) for p, i in PDs])]
    SQs = [q for _, q in sorted([(i, q) for q, i in QDs])]

    err = [0] * 100
    sig = [0] * 10000
    for p in range(100):
        for q in range(10000):
            sig[q] = '1' if random.random() <= f(SPs[p], SQs[q]) else '0'
        err[p] = error(Rs[p], sig)

    Es = sorted((e, i) for i, e in enumerate(err))
    E = [e for _, e in sorted([(i, e) for e, i in Es])]
    return Es[-1][1]+1

T = int(input())
P = int(input())
for x in range(1, T+1):
    Rs = [input() for _ in range(100)]
    print(f"Case #{x}: {cheater(Rs)}")
