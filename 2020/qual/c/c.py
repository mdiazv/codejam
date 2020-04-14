
class Worker:
    def __init__(self, name):
        self.busy_until = 0
        self.name = name

def free(W, t):
    for w in W:
        if w.busy_until <= t:
            return w

def assign(N, As):
    W = set([Worker('C'), Worker('J')])
    ordered = ''
    for (start, end, i) in As:
        w = free(W, start)
        if w is None:
            return 'IMPOSSIBLE'
        ordered += w.name
        w.busy_until = end

    R = [0 for _ in range(N)]
    for a, w in zip(As, ordered):
        R[a[2]] = w
        
    return ''.join(R)

T = int(input())
for x in range(1, T+1):
    N = int(input())
    As = sorted([list(map(int, input().split()))+[i] for i in range(N)])
    R = assign(N, As)
    print ("Case #{}: {}".format(x, R))
