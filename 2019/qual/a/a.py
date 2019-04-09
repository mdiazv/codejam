
T = int(input())
for x in range(1, T+1):
    N = input()
    A = ''
    B = ''
    for c in N:
        if c == '4':
            A += '3'
            B += '1'
        else:
            A += c
            B += '0'
    print("Case #{}: {} {}".format(x, int(A), int(B)))
