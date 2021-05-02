from itertools import takewhile

def process(a, b):
    if int(a) < int(b):
        return 0, b
    add, target = 0, str(int(a)+1)
    while len(b) < len(target):
        if b == target[:len(b)]:
            b += target[len(b)]
        else:
            b += '0'
        add += 1
    if int(a) >= int(b):
        b += '0'
        add += 1
    return add, b

def solve(N, Xs):
    ops = 0
    for k in range(1, N):
        add, new = process(Xs[k-1], Xs[k])
        ops += add
        Xs[k] = new
    return ops

T = int(input())
for x in range(1, T+1):
    N = int(input())
    Xs = input().split()
    print (f"Case #{x}: {solve(N, Xs)}")
