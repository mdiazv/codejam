
def can_flip(S, k, i):
    return i >= 0 and i <= len(S) - k

def flip(S, k, i):
    rev = ''.join(['-' if c == '+' else '+' for c in S[i:i+k]])
    return S[:i] + rev + S[i+k:]

def min_flip(S, k):
    n = 0
    for i in xrange(0, len(S)):
        if S[i] == '-':
            if can_flip(S, k, i):
                S = flip(S, k, i)
                n += 1
    return n if S == '+'*len(S) else -1


T = int(raw_input())
for x in xrange(1, T+1):
    S, K = raw_input().split()
    k = int(K)

    r = min_flip(S, k)
    print "Case #{}: {}".format(x, r if r >= 0 else 'IMPOSSIBLE')
