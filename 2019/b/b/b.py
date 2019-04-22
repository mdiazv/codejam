class Stone:
    def __init__(self, s, e, l):
        self.s, self.e, self.l = s, e, l
    def __repr__(self):
        return "Stone<{s.s}, {s.e}, {s.l}, Energy {e}>".format(s=self,e=self.energy())
    def energy(self, t):
        return max(0, self.e - self.l * t)
    def __lt__(self, other):
        return self.s * other.l < other.s * self.l

def solve(N, S):
    DP = [{} for _ in range(N)]
    def dp(i, t):
        if i == N:
            return 0
        if t in DP[i]:
            return DP[i][t]

        e = S[i].energy(t)
        take = e + dp(i+1, t+S[i].s)
        skip = dp(i+1, t)

        DP[i][t] = max(take, skip)
        return DP[i][t]

    return dp(0, 0)

T = int(input())
for x in range(1, T+1):
    N = int(input())
    S = []
    for _ in range(N):
        s, e, l = map(int, input().split())
        S.append(Stone(s, e, l))
    print ("Case #{}: {}".format(x, solve(N, list(sorted(S)))))
