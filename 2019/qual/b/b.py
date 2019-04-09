
T = int(input())
for x in range(1, T+1):
    N = int(input())
    P = input()
    b = ''.join('S' if c == 'E' else 'E' for c in P)
    print('Case #{}: {}'.format(x, b))
