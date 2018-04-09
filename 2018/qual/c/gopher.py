from itertools import cycle
import sys


T = int(input())
for _ in range(1, T+1):
    A = int(input())
    L = set((2, 2+x) for x in range(A//3 + A%3))
    R = cycle(L)
    H = {}
    for x in range(1001):
        done = False
        while not done:
            i, j = R.__next__()
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if (i+di, j+dj) not in H:
                        done = True
                        break
            if not done:
                L.remove((i, j))
                R = cycle(L)

        print ('{} {}'.format(i, j))
        ri, rj = map(int, input().split())
        if ri == -1 and rj == -1:
            #print ('Judge killed us', file=sys.stderr)
            sys.exit(1)
        if ri == 0 and rj == 0:
            #print ('Case solved. A: {}, x: {}'.format(A, x), file=sys.stderr)
            break
        H[(ri, rj)] = x

#print ('best: {}, worst: {}, avg: {}'.format(min(stats), max(stats), sum(stats) / len(stats)), file=sys.stderr)
