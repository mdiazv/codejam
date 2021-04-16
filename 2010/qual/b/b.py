
T = int(input())
for x in range(1, T+1):
    N, K = map(int, input().split())
    y = "ON" if bin(K)[-N:] == '1'*N else "OFF"
    print (f"Case #{x}: {y}")
