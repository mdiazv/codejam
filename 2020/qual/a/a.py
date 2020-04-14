def column(matrix, i):
    return [row[i] for row in matrix]

T = int(input())
for x in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    k = sum(M[i][i] for i in range(N))
    r = sum(len(set(row)) != N for row in M)
    c = sum(len(set(column(M, i))) != N for i in range(N))
    print ("Case #{}: {} {} {}".format(x, k, r, c))

