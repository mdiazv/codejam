
def brute(E, W, X):
    visited = set()
    queue = [(0, 0, ())]
    while queue:
        (steps, e, stk), queue = queue[0], queue[1:]
        if e == E:
            return steps+len(stk)
        if (e, stk) in visited:
            continue
        visited.add( (e, stk) )
        Cs = [0] * W
        for w in stk:
            Cs[w] += 1

        # complete
        if Cs == X[e]:
            queue.append( (steps, e+1, stk) )
            continue

        # pop
        queue.append( (steps+1, e, stk[:-1]) )

        # add
        for i, c in enumerate(Cs):
            if c < X[e][i]:
                queue.append( (steps+1, e, stk + (i,)) )

    return -1

def solve(E, W, X):
    return brute(E, W, X)

T = int(input())
for x in range(1, T+1):
    E, W = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(E)]
    y = solve(E, W, X)
    print (f'Case #{x}: {y}')

