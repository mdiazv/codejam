import statistics
import random

def cheater(Rs):
    Qs = [0] * 10000
    ok = []
    for r in Rs:
        k = 0
        for i, v in enumerate(r):
            Qs[i] += v == '1'
            k += v == '1'
        ok.append(k)
    PQs = [q/100 for q in Qs]
    std = []
    for i, r in enumerate(Rs):
        bad = 10000 - ok[i]
        #score_ok = sum(1-q for ok, q in zip(r, PQs) if ok) / ok
        score_ok = statistics.median(1-q for ok, q in zip(r, PQs) if ok == '1')
        score_bad = statistics.median(1-q for ok, q in zip(r, PQs) if ok == '0')
        #var_ok = statistics.pvariance(q for ok, q in zip(r, PQs) if ok)
        #var_bad = statistics.pvariance(q for ok, q in zip(r, PQs) if not ok)
        #print ("stdnt", i, "ok", ok, "bad", bad, "score_ok", score_ok, "score_bad", score_bad)
        #print ("stdnt", i, "var_ok", var_ok, "var_bad", var_bad)
        std.append((ok[i], score_ok, score_bad, i))

    print (sorted(std)[-3:])
    t = random.choice(sorted(std)[-3:])
    return t[3]+1

T = int(input())
P = int(input())
for x in range(1, T+1):
    Rs = [input() for _ in range(100)]
    print(f"Case #{x}: {cheater(Rs)}")
