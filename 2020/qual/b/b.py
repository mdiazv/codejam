
def nest(S):
    R = ""
    d = 0
    for c in S:
        k = int(c)
        if k > d:
            R += "(" * (k-d)
        if k < d:
            R += ")" * (d-k)
        R += c
        d = k
    R += ")" * d
    return R

T = int(input())
for x in range(1, T+1):
    S = input()
    R = nest(S)
    print ("Case #{}: {}".format(x, R))
