
T = int(input())
for x in range(1, T+1):
    D, N = map(int, input().split(' '))
    A = []
    for _ in range(N):
        k, s = map(int, input().split(' '))
        A.append((D-k) / s)
    speed = D / max(A)
    print ('Case #{}: {}'.format(x, speed))
