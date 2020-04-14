
class Floor:
    def __init__(self, R, C, M):
        self.R = R
        self.C = C
        self.M = M
        self.base_int = sum(M[i][j] for i in range(R) for j in range(C))
        self.current_int = self.base_int
        self.total_int = self.base_int
        self.remaining = {(i, j): [(di, dj) for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]
                                    if i+di >= 0 and j+dj >= 0 and i+di < R and j+dj < C
                                        and di != dj and (di == 0 or dj == 0)
                                  ] for i in range(R) for j in range(C)
                         }
        self.alive = R*C
    def __repr__(self):
        return "{}".format(self.remaining)

    def ray(self, i, j, di, dj):
        while (i+di, j+dj) not in self.remaining and i+di >= 0 and j+dj >= 0 and i+di < self.R and j+dj < self.C:
            if di > 0:
                di += 1
            if di < 0:
                di -= 1
            if dj > 0:
                dj += 1
            if dj < 0:
                dj -= 1
        return (di, dj) if (i+di, j+dj) in self.remaining else (0, 0)

    def nextgen(self):
        start = self.alive
        V = [[0] * self.C for _ in range(self.R)]
        elim = []
        alone = []
        for (i, j), nbs in self.remaining.items():
            nnb = []
            for nb in nbs:
                di, dj = r = self.ray(i, j, *nb)
                if r != (0, 0):
                    nnb.append( (di, dj) )
            if nnb:
                avg = sum(M[i+di][j+dj] for di, dj in nnb) / len(nnb)
                if M[i][j] < avg:
                    elim.append( (i, j) )
                self.remaining[i, j] = nnb
            else:
                # saved
                alone.append( (i, j) )

        for i, j in elim:
            self.current_int -= M[i][j]
            self.alive -= 1
            del self.remaining[i, j]
            M[i][j] = 0

        for i, j in alone:
            del self.remaining[i, j]

        if self.alive == start:
            return False

        self.total_int += self.current_int
        return True

    def run(self):
        while self.nextgen():
            pass
        return self.total_int


def total_interest(M, R, C):
    F = Floor(R, C, M)
    return F.run()


T = int(input())
for x in range(1, T+1):
    R, C = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(R)]
    I = total_interest(M, R, C)
    print("Case #{}: {}".format(x, I))
