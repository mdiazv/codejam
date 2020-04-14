from functools import lru_cache
import heapq as H

@lru_cache(10000000)
def get(r, k):
    if k == 1 or k == r:
        return 1
    return get(r-1, k-1) + get(r-1, k)

def neighbors(ri, ki):
    return list(filter(lambda t: t[0] >= 1 and t[1] >= 1 and t[1] <= t[0],
        [(ri - 1, ki - 1), (ri - 1, ki), (ri, ki - 1), (ri, ki + 1), (ri + 1, ki), (ri + 1, ki + 1)]
    ))


def walk(N):
    heap = [(-1, set([(1, 1)]), [(1, 1)])]
    while heap:
        s, visited, order = H.heappop(heap)
        r, k = order[-1]
        if -s == N:
            return order
        if -s > N:
            continue
        for rn, kn in neighbors(r, k):
            if (rn, kn) not in visited:
                H.heappush(heap, (s - get(rn, kn), visited | set([(rn, kn)]), order + [(rn, kn)]))


T = int(input())
for x in range(1, T+1):
    N = int(input())
    print("Case #{}:".format(x))
    for a, b in walk(N):
        print (a, b)

