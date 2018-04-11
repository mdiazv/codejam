from collections import defaultdict, deque
import sys

sys.setrecursionlimit(200000)

class Graph:
    def __init__(self):
        self.v = set()
        self.e = defaultdict(list)
        self.r = defaultdict(list)
    def add(self, a, b):
        self.v.add(a)
        self.v.add(b)
        self.e[a].append(b)
        self.r[b].append(a)
    def components(self):
        L = deque()
        visited = set()
        def visit(u):
            if u not in visited:
                visited.add(u)
                for v in self.e[u]:
                    visit(v)
                L.appendleft(u)

        order = []
        assigned = set()
        cs = defaultdict(set)
        def assign(u, root):
            if u not in assigned:
                assigned.add(u)
                if root not in cs:
                    order.append(root)
                cs[root].add(u)
                for v in self.r[u]:
                    assign(v, root)

        for u in self.v:
            visit(u)
        for u in L:
            assign(u, u)

        return [cs[c] for c in order]

class TwoSat:
    def __init__(self):
        self.cs = None
    def is_satisfiable(self, clauses):
        g = Graph()
        for p, q in clauses:
            g.add(-p, q)
            g.add(-q, p)

        cs = g.components()
        for c in cs:
            for v in c:
                if -v in c:
                    return False
        
        self.cs = cs
        return True
    def assignment(self):
        if self.cs is None:
            raise Exception('No components')

        a = set()
        for c in reversed(self.cs):
            for v in c:
                if v not in a and -v not in a:
                    a.add(v)
        return a

class CNFEncoder:
    def __init__(self, solver):
        self.solver = solver
        self.forward_map = {}
        self.reverse_map = {}
        self.clauses = []
    def add(self, o1, v1, o2, v2):
        self.clauses.append((self._encode(o1) * self._sign(v1), self._encode(o2) * self._sign(v2)))
    def solve(self):
        if self.solver.is_satisfiable(self.clauses):
            return map(self._decode, self.solver.assignment())
    def _encode(self, obj):
        if obj not in self.forward_map:
            key = 1 + len(self.forward_map)
            self.forward_map[obj] = key
            self.reverse_map[key] = obj
        return self.forward_map[obj]
    def _decode(self, key):
        return self.reverse_map[abs(key)], key > 0
    def _sign(self, val):
        return {True: 1, False: -1}[val]


R, C = 0, 0


def _fire(M, i, j, di, dj, acc):
    ni, nj = i + di, j + dj
    if ni < 0 or ni >= R or nj < 0 or nj >= C:
        return acc
    if M[ni][nj] == '#':
        return acc
    if M[ni][nj] == '.':
        acc.append((ni, nj))
        return _fire(M, ni, nj, di, dj, acc)
    if M[ni][nj] in '-|':
        return None
    if M[ni][nj] == '/':
        return _fire(M, ni, nj, -dj, -di, acc)
    if M[ni][nj] == '\\':
        return _fire(M, ni, nj, dj, di, acc)
    raise Exception('Nani?')

def fire(M, i, j, d):
    if d == '-':
        pr = _fire(M, i, j, 0,  1, [])
        pl = _fire(M, i, j, 0, -1, [])
        return None if pr is None or pl is None else pr + pl
    else:
        pu = _fire(M, i, j, -1, 0, [])
        pd = _fire(M, i, j,  1, 0, [])
        return None if pu is None or pd is None else pu + pd

def negate(c):
    return '-' if c == '|' else '|'

def solve(M):
    blank = {}
    laser = {}
    for i, r in enumerate(M):
        for j, c in enumerate(r):
            if c == '.':
                blank[(i, j)] = []
            elif c in '-|':
                laser[(i, j)] = c

    solver = CNFEncoder(TwoSat())
    for l in laser:
        paths = [fire(M, *l, '-'), fire(M, *l, '|')]
        which = 0
        for i, (path, dir) in enumerate(zip(paths, '-|')):
            if path is not None:
                which |= i+1
                for dot in path:
                    blank[dot].append((l, dir))
        if which == 0:
            print ('Laser at {} will always hit a laser'.format(l), file=sys.stderr)
            return []
        if which == 1:
            solver.add(l, False, l, False)
        elif which == 2:
            solver.add(l, True, l, True)

    for dot, options in blank.items():
        if not options:
            print ('Dot at {} can not be covered'.format(dot), file=sys.stderr)
            return []
        if len(options) == 1:
            l, dir = options[0]
            solver.add(l, dir == '|', l, dir == '|')
        elif len(options) == 2:
            l0, d0 = options[0]
            l1, d1 = options[1]
            solver.add(l0, d0 == '|', l1, d1 == '|')
        else:
            print ('There are {} options for {}'.format(len(options), dot), file=sys.stderr)
            return []

    solution = solver.solve()
    if not solution:
        print ('Solver says no soup for you', file=sys.stderr)
        return []

    for (i, j), is_vertical in solution:
        M[i][j] = '|' if is_vertical else '-'

    return M


T = int(input())
for x in range(1, T+1):
    R, C = map(int, input().split())
    M = [list(input()) for _ in range(R)]
    R = solve(M)
    print ('Case #{}: {}'.format(x, 'POSSIBLE' if R else 'IMPOSSIBLE'))
    for m in R:
        print (''.join(m))
