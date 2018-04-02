from operator import itemgetter
from string import ascii_uppercase

def evacuate(N, P):
    steps = []
    members = sum(map(itemgetter(0), P))
    parties = N
    while members > 0:
        if parties == 1:
            print ("ERROR: only one party left")
            return steps

        ps = list(reversed(sorted(P)))
        gap = ps[0][0] - ps[1][0]
        if parties == 2:
            steps += [ps[0][1]] * gap
            steps += [ps[0][1] + ps[1][1]] * ps[0][0]
            members = 0
            parties = 0
        else:
            if gap == 0:
                if parties > 3:
                    steps.append(ps[0][1] + ps[1][1])
                    members -= 2
                    ps[0] = (ps[0][0] - 1, ps[0][1])
                    ps[1] = (ps[1][0] - 1, ps[1][1])
                    if ps[0][0] == 0:
                        parties -= 2
                else:
                    steps.append(ps[0][1])
                    members -= 1
                    ps[0] = (ps[0][0] - 1, ps[0][1])
                    if ps[0][0] == 0:
                        parties -= 1
            else:
                steps += [ps[0][1]] * gap
                ps[0] = (ps[0][0] - gap, ps[0][1])
                members -= gap
        P = ps

    return steps


T = int(input())
for x in range(1, T+1):
    N = int(input())
    P = zip(map(int, input().split(' ')), ascii_uppercase)
    steps = evacuate(N, list(P))
    print('Case #{}: {}'.format(x, ' '.join(steps)))
