from functools import reduce

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def doomsday(Ts):
    g = reduce(gcd, [abs(Ts[0]-t) for t in Ts[1:]])
    return 0 if Ts[0] % g == 0 else g - (Ts[0] % g)

C = int(input())
for x in range(1, C+1):
    Ts = list(map(int, input().split()))
    N, Ts = Ts[0], Ts[1:]
    print (f"Case #{x}: {doomsday(Ts)}")
