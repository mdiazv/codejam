
def switches(S, Q, Qry):
    sw, unseen = 0, set(range(S))
    for q in Qry:
        if q in unseen:
            unseen.remove(q)
        if not unseen:
            sw += 1
            unseen = set(range(S))
            unseen.remove(q)
    return sw

N = int(input())
for x in range(1, N+1):
    S = int(input())
    Eng = {input(): i for i in range(S)}
    Q = int(input())
    Qry = [Eng[input()] for _ in range(Q)]
    y = switches(S, Q, Qry)
    print (f"Case #{x}: {y}")
