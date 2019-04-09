import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def sieve(n):
    primes = set()
    not_primes = set()
    for x in range(2, n+1):
        if x in not_primes:
            continue
        primes.add(x)
        for k in range(x, n+1, x):
            not_primes.add(k)
    return primes

def gen():
    s = ''
    L = set()
    while any(c not in L for c in letters):
        c = random.choice(letters)
        s += c
        L.add(c)
        if int(random.uniform(0, 10)) <= 2:
            s += c * int(random.uniform(1, 3))
        elif int(random.uniform(0, 10)) <= 2:
            d = random.choice(letters)
            s += (c+d) * int(random.uniform(1, 3))
            L.add(d)
    return s

T = 500
MAXN = 10**7
primes = sieve(MAXN)

with open('leX.in', 'w') as le_in:
    with open('leX.out', 'w') as le_out:
        print (T, file=le_in)
        for x in range(1, T+1):
            N = int(random.uniform(101, MAXN))
            s = gen()
            P = list(sorted(random.sample(primes, 26)))
            D = {c: P[i] for i, c in enumerate(letters)}
            C = [D[a] * D[b] for a, b in zip(s, s[1:])]

            print(N, len(C), file=le_in)
            for c in C:
                print(c, end=' ', file=le_in)
            print(file=le_in)
            print('Case #{}: {}'.format(x, s), file=le_out)
