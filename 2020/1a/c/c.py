
LEFT  = (-1, 0)
RIGHT = ( 1, 0)
UP    = ( 0,-1)
DOWN  = ( 0, 1)
DIRECTIONS = [LEFT, UP, RIGHT, DOWN]

class Floor:
    def __init__(self, M, R, C):
        self.M, self.R, self.C = M, R, C
        self.gen = 1
        self.base_score = sum(M[i][j] for i in range(R) for j in range(C))
        self.current_score = self.base_score
        self.total_score = self.base_score
        self.remaining = {
            (i, j): {(di, dj): (i+di, j+dj) for di, dj in DIRECTIONS if self.in_bounds(i+di, j+dj)}
            for i in range(R) for j in range(C)
        }
        self.modified = set((i, j) for i in range(R) for j in range(C))
    def __repr__(self):
        s = "Gen {}\n".format(self.gen)
        s += "\n".join(" ".join(map(str, row)) for row in self.M)
        s += "\nRemaining: "+repr(self.remaining)
        s += "\nModified: "+repr(self.modified)
        s += "\nScore - current:{} - total:{}".format(self.current_score, self.total_score)
        return s
    def in_bounds(self, i, j):
        return i >= 0 and j >= 0 and i < self.R and j < self.C
    def eliminated(self, i, j):
        nbs = [M[ni][nj] for _, (ni, nj) in self.remaining[i, j].items()]
        avg = sum(nbs) / len(nbs) if nbs else 0
        return M[i][j] < avg
    def nextgen(self):
        modified, eliminated = set(), set()
        for i, j in self.modified:
            if self.eliminated(i, j):
                eliminated.add( (i, j) )
            
        if not eliminated:
            return False

        score = 0
        for i, j in eliminated:
            for d, nb in self.remaining[i, j].items():
                inv = (-d[0], -d[1])
                nbi = self.remaining[i, j].get(inv, None)
                # update neighbors in both directions
                if nbi:
                    self.remaining[nbi][d] = nb
                    self.remaining[nb][inv] = nbi
                    modified.add(nb)
                    modified.add(nbi)
                elif inv in self.remaining[nb]:
                    del self.remaining[nb][inv]
                    modified.add(nb)

            score += M[i][j]
            M[i][j] = 0
            del self.remaining[i, j]

        self.current_score = self.base_score - score
        self.base_score = self.current_score
        self.total_score += self.current_score
        self.modified = modified - eliminated
        self.gen += 1
        return True

    def run(self):
        while self.nextgen():
            pass
        return self.total_score


def total_interest(M, R, C):
    F = Floor(M, R, C)
    return F.run()

T = int(input())
for x in range(1, T+1):
    R, C = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(R)]
    I = total_interest(M, R, C)
    print("Case #{}: {}".format(x, I))
