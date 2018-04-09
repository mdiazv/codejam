
def damage(s):
    d = 0
    p = 1
    for c in s:
        if c == 'C':
            p *= 2
        else:
            d += p
    return d
    
T = int(input())
for x in range(1, T+1):
    N, S = input().split()
    D = int(N)
    d = damage(S)
    s = 0
    while d > D and 'C' in S:
        # Trim all C to the right
        p = S.rfind('S')
        S = S[:p+1]
        
        # Swap the rightmost C
        p = S.rfind('C')
        S = S[:p] + S[p+1] + S[p] + S[p+2:]

        d = damage(S)
        s += 1

    print ("Case #{}: {}".format(x, s if d <= D else 'IMPOSSIBLE'))
