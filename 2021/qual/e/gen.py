import math
import random

def f(p, q):
    x = p - q
    return 1 / (1 + math.exp(-x))

Ps = [random.uniform(-3, 3) for _ in range(100)]
Qs = [random.uniform(-3, 3) for _ in range(10000)]
c = random.randint(0, 99)

Rs = []
p = [0] * 10000
cheats = []
for k in range(100):
    for q in range(10000):
        if k == c and random.randint(0, 1):
            p[q] = '1'
            cheats.append( (q, Qs[q], f(Ps[k], Qs[q]), random.random() <= f(Ps[k], Qs[q])) )
            continue
        p[q] = '1' if random.random() <= f(Ps[k], Qs[q]) else '0'
    Rs.append(p.copy())

with open('gen.in', 'w') as f:
    print ('1', file=f)
    print ('0', file=f)
    for k in range(100):
        print (''.join(Rs[k]), file=f)

with open ('gen.out', 'w') as f:
    print (f'Case #1: {c+1}', file=f)

print ("Cheater player", c)
print ("Cheater skill", Ps[c])
print ("Total cheats", len(cheats))
print ("Actual benefits", sum(not cheat[3] for cheat in cheats))

QDs = sorted([(q, i) for i, q in enumerate(Qs)])

SRs = []
for k in range(100):
    for q in range(10000):
        p[q] = Rs[k][QDs[q][1]]
    SRs.append(p.copy())

#for i, r in enumerate(SRs):
#    print (i, ''.join(r))
