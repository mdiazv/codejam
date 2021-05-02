
def solve(N, Xs):
    ops = 0
    for k in range(1, N):
        while int(Xs[k-1]) >= int(Xs[k]):
            for c in "0123456789":
                if int(Xs[k]+c) > int(Xs[k-1]):
                    Xs[k] += c
                    ops += 1
                    break
            else:
                Xs[k] += '0'
                ops += 1
    return ops

T = int(input())
for x in range(1, T+1):
    N = int(input())
    Xs = input().split()
    print (f"Case #{x}: {solve(N, Xs)}")
