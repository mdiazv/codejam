
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def mapping(decoded):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    values = sorted(set(decoded))
    return {v: l for v, l in zip(values, letters)}

def decode(N, L, Cipher):
    def bt(i, prev=None):
        if i == L:
            return []

        a = Cipher[i]
        if prev:
            c = a // prev
            return [c] + bt(i+1, c)

        b = Cipher[i+1]
        if a != b:
            c = gcd(a, b)
            return [a // c, c] + bt(i+1, c)

        rest = bt(i+1, None)
        c = a // rest[0]
        return [c] + rest

    decoded = bt(0, None)
    M = mapping(decoded)
    return ''.join(M[c] for c in decoded)

T = int(input())
for x in range(1, T+1):
    N, L = map(int, input().split())
    Cipher = list(map(int, input().split()))
    print('Case #{}: {}'.format(x, decode(N, L, Cipher)))
