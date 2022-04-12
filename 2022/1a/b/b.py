
def solve(A, B, N):
    s1, s2, S1, S2 = 0, 0, [], []
    C = sorted(A+B, reverse=True)
    for c in C:
        if s1 > s2:
            S2.append(c)
            s2 += c
        else:
            S1.append(c)
            s1 += c
    return S1

def generate(N):
    A = [2 ** k for k in range(30)]
    return A + [10**9-k for k in range(N-len(A))]

T = int(input())
for x in range(1, T+1):
    N = int(input())
    if N == -1:
        break
    A = generate(N)
    print (' '.join(map(str, A)))
    B = list(map(int, input().split()))
    S = solve(A, B, N)
    print (' '.join(map(str, S)))

