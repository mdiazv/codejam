import math


class Vector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def _add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def mult(self, v):
        return Vector(self.x * v, self.y * v, self.z * v)
    def mod(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    def __repr__(self):
        return "<{:.3f}, {:.3f}, {:.3f}>".format(self.x, self.y, self.z)


def best(P, V):
    t = 0
    if V.mod():
        t = max(0, (-P.x*V.x -P.y*V.y -P.z*V.z) / (V.x*V.x + V.y*V.y + V.z * V.z))
    d = P.add(V.mult(t)).mod()
    return d, t


T = int(input())
for x in range(1, T+1):
    N = int(input())
    P, V = Vector(0, 0 ,0), Vector(0, 0, 0)
    for _ in range(N):
        b = list(map(int, input().split()))
        p, v = Vector(*b[:3]), Vector(*b[3:])
        P._add(p)
        V._add(v)
    d, t = best(P.mult(1/N), V.mult(1/N))
    print ("Case #{}: {} {}".format(x, d, t))
