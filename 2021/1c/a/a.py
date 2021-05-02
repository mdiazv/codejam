
def buy(N, K, Ps):
    single = []
    double = []
    if Ps[0] > 1:
        single.append( (Ps[0]-1, 0, Ps[0]) )
    k = Ps[0]
    for p in Ps[1:]:
        if k+1 < p:
            single.append( ((p-k)//2, k, p) )
            double.append( (p-k-1, k, p) )
        k = p
    if Ps[-1] < K:
        single.append( (K-Ps[-1], Ps[-1], K) )

    single = sorted(single)
    double = sorted(double)

    return max(sum(s[0] for s in single[-2:]), sum(d[0] for d in double[-1:])) / K

T = int(input())
for x in range(1, T+1):
    N, K = map(int, input().split())
    Ps = sorted(map(int, input().split()))
    p = buy(N, K, Ps)
    print(f"Case #{x}: {p}")
