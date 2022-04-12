from collections import defaultdict
import operator
import sys
sys.setrecursionlimit(100001)

def solve(N, Ff, Ps):
    Cs = defaultdict(list)
    for i in range(N):
        Cs[Ps[i]-1].append(i)
    Cs = dict(Cs)
    Ac = set(c for c in range(N) if c not in Cs)

    def find_activator(n):
        # elegant but stack hungry
        if n not in Cs:
            return Ff[n], [n]

        f, ks = min(map(find_activator, Cs[n]))
        return max(f, Ff[n]), ks+[n]

    def reduce(k, fn, default):
        r = default
        while k != -1:
            r = fn(r, k)
            k = Ps[k]-1
        return r

    def find_activator2(n):
        def sumFf(r, k):
            return r + Ff[k]
        def chain(r, k):
            r.append(k); return r
        def maxFf(r, k):
            return max(r, Ff[k])
        s, n = min((reduce(k, sumFf, 0), k) for k in Ac)
        return reduce(n, maxFf, -1), reduce(n, chain, [])

    def activate(chain):
        Ac.remove(chain[0])
        sc = set(chain)
        for n in chain:
            Ff[n] = 0
            Ps[n] = 0
            if n in Cs:
                for c in Cs[n]:
                    Ps[c] = 0
                    if c not in sc:
                        Cs[-1].append(c)

    score = 0
    while Cs[-1]:
        root = Cs[-1].pop()
        s, chain = find_activator(root)
        score += s
        activate(chain)
    return score
    

T = int(input())
for x in range(1, T+1):
    N = int(input())
    Ff = list(map(int, input().split()))
    Ps = list(map(int, input().split()))
    best = solve(N, Ff, Ps)
    print (f'Case #{x}: {best}')
