from math import sin, cos, sqrt, radians, degrees, acos
import sys

epsilon = 10 ** (-9)

class AngleFinder:
    SIDE = sin(radians(45))
    def __init__(self, A):
        self.A = A
        self.single_rot = A <= 1.414213
    def angles(self, x):
        return (x, 0) if self.single_rot else (45, x)
    def project(self, x):
        return 2 * self.SIDE * cos(radians(45 - x))
    def area(self, x):
        a, b = self.angles(x)
        return self.project(a) * self.project(b)
    def find(self):
        #print ('looking for angle to get area: {}'.format(self.A), file=sys.stderr)
        def f(lower, upper):
            h = (lower + upper) / 2
            a = self.area(h)
            if abs(self.A-a) < epsilon:
                #print('area: {}'.format(a), file=sys.stderr)
                return h
            if a < self.A:
                return f(h, upper)
            if a > self.A:
                return f(lower, h)
            raise Exception("Nani?")
        angle = f(0, 45)
        angles = self.angles(angle)
        #print('angle: {} -> {}'.format(angle, angles), file=sys.stderr)
        return angles

class Vector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def rotateX(self, angle):
        a = radians(angle)
        return Vector(
            self.x,
            self.y * cos(a) - self.z * sin(a),
            self.y * sin(a) + self.z * cos(a)
        )
    def rotateY(self, angle):
        a = radians(angle)
        return Vector(
            self.x * cos(a) + self.z * sin(a),
            self.y,
            -self.x * sin(a) + self.z * cos(a)
        )
    def rotateZ(self, angle):
        a = radians(angle)
        return Vector(
            self.x * cos(a) - self.y * sin(a),
            self.x * sin(a) + self.y * cos(a),
            self.z
        )
    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z
    def angle(self, v):
        cos_a = self.dot(v) / (self.length() * v.length())
        return degrees(acos(cos_a))
    def __repr__(self):
        return "<{:.9f} {:.9f} {:.9f}>".format(self.x, self.y, self.z)
    def __str__(self):
        return "{:.9f} {:.9f} {:.9f}".format(self.x, self.y, self.z)

def rotate(a, b):
    vs = [
        Vector(0.5, 0, 0),
        Vector(0, 0.5, 0),
        Vector(0, 0, 0.5),
    ]
    vx = [v.rotateX(a) for v in vs]
    vz = [v.rotateZ(b) for v in vx]
    return vz

def test(vs):
    for v in vs:
        if abs(v.length() - 0.5) > epsilon:
            raise Exception("Distance is wrong for: {} ({})".format(v, v.length()))
    if (abs(vs[0].angle(vs[1]) - 90) > epsilon
     or abs(vs[0].angle(vs[2]) - 90) > epsilon
     or abs(vs[1].angle(vs[2]) - 90) > epsilon):
        raise Exception("Bad angles")

def random_test():
    import random
    for _ in range(5000):
        A = random.uniform(1.0, 2.0)
        f = AngleFinder(A)
        a, b = f.find()
        vs = rotate(a, b)
        test(vs)

T = int(input())
for x in range(1, T+1):
    A = float(input())
    f = AngleFinder(A)
    a, b = f.find()
    vs = rotate(a, b)

    print ('Case #{}:'.format(x))
    for v in vs:
        print(v)
