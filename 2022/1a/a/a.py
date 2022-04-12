
def solve(S):
    R = ''
    streak = ''
    for a, b in zip(S, S[1:]):
        if a == b:
            streak += a
            #print (f'{a} == {b} => streak {streak}')
        elif a > b:
            R += streak+a
            streak = ''
            #print (f'{a} > {b} => streak {streak}')
        else:
            R += (streak+a)*2
            #print (f'{a} < {b} => streak {streak}')
            streak = ''
        #print (R)

    return R + streak + S[-1]


T = int(input())
for x in range(1, T+1):
    S = input()
    print (f'Case #{x}: {solve(S)}')
