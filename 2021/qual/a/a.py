
def revsort(N, L):
    cost = 0
    for i in range(N-1):
        c = L[i:].index(min(L[i:]))+1
        L = L[:i] + list(reversed(L[i:i+c])) + L[i+c:]
        cost += c
    return cost

T = int(input())
for x in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    cost = revsort(N, L)
    print (f"Case #{x}: {cost}")
