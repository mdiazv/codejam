
def FastTroubleSort(L):
    even = sorted(L[::2])
    odd = sorted(L[1::2])
    LE = len(even)
    LO = len(odd)
    for i in range(len(L)//2 + len(L)%2):
        if i < LE:
            yield even[i]
        if i < LO:
            yield odd[i]

def FirstUnsorted(L):
    prev = -1
    for i, e in enumerate(L):
        if prev > e:
            return i-1
        prev = e
    return 'OK'

T = int(input())
for x in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    R = FirstUnsorted(FastTroubleSort(L))
    print ('Case #{}: {}'.format(x, R))
