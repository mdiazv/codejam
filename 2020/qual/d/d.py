import sys

NOOP = 0
FLIP = 1
REVE = 2
REFL = 3

def do(op, S):
    if op == NOOP:
        return S
    if op == FLIP:
        return ['-' if c == '-' else str(1 - int(c)) for c in S]
    if op == REVE:
        return S[::-1]
    if op == REFL:
        return do(1, do(2, S))

def solve(B):
    S = ['-' for _ in range(B)]
    k = 0
    ks = 0
    while k < 150:
        if '-' not in S:
            return ''.join(S)

        assert k % 10 == 0
        peq = [(i, a) for i, (a, b) in enumerate(zip(S, reversed(S))) if a != '-' and a == b]
        pne = [(i, a) for i, (a, b) in enumerate(zip(S, reversed(S))) if a != '-' and a != b]
        pos = set([NOOP, FLIP, REVE, REFL])
        
        if peq:
            i, v = peq[0]
            print(i+1)
            bi = input()
            pos &= set([NOOP, REVE] if bi == v else [FLIP, REFL])
            k += 1

        if pne:
            i, v = pne[0]
            print(i+1)
            bi = input()
            pos &= set([NOOP, REFL] if bi == v else [FLIP, REVE])
            k += 1

        if len(pos) == 1:
            S = do(next(iter(pos)), S)
        elif len(pos) == 2 and FLIP in pos:
            S = do(FLIP, S)

        while k == 0 or (k % 10 not in {9, 0} and '-' in S):
            print (ks+1)
            print (B-ks)
            S[ks] = input()
            S[B-ks-1] = input()
            ks += 1
            k += 2

        if k % 10 == 9:
            print (1)
            input()
            k += 1

    return ''.join(S)

T, B = map(int, input().split())
for _ in range(T):
    print(solve(B))
    r = input()
    if r == "N":
        break
