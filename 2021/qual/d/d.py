import sys

class Guess:
    def __init__(self, N, Q):
        self.N, self.Q = N, Q
        self.reset()
    def reset(self):
        self.k = 0
        self.half = -1
        self.knows = []
        self.plays = []
        self.replies = []
        self.search = None
    def query(self):
        if not self.knows:
            self.last = (1,2,3)
        elif not self.search:
            self.search = [0, len(self.knows)-1]
            print ("Starting new search!", self.search, file=sys.stderr)

        if self.search:
            if self.search[1] - self.search[0] > 8:
                self.third = (self.search[1] - self.search[0]) // 3
                print ("Trying thirds!", self.knows, self.search, self.third, file=sys.stderr)
                self.last = (self.knows[self.search[0]+self.third],
                             self.knows[self.search[0]+2*self.third],
                             len(self.knows)+1)
            else:
                self.half = (self.search[1] + self.search[0]) // 2
                self.last = (self.knows[self.half], self.knows[self.half+1], len(self.knows)+1)

        self.Q -= 1
        print ("Querying", self.last, "half", self.half, file=sys.stderr)
        self.plays.append((self.last, self.search.copy() if self.search else None))
        self.k += 1
        return self.last
    def update(self, median):
        print ("Median for", self.last, "is", median, file=sys.stderr)
        self.replies.append(median)
        if not self.knows:
            if median == 1:
                self.knows = [2,1,3]
            elif median == 3:
                self.knows = [1,3,2]
            else:
                self.knows = [1,2,3]
            print ("Opening move! Learned something", self.knows, file=sys.stderr)
        elif self.search[1] - self.search[0] > 8:
            print ("Third leap! before", self.search, self.third, file=sys.stderr)
            if median == self.last[2]:
                self.search = [self.search[0]+self.third, self.search[0]+2*self.third]
            elif median == self.last[1]:
                self.search[0] = self.search[0]+2*self.third
            else:
                self.search[1] = self.search[0]+self.third
            print ("Third leap! after", self.search, self.third, file=sys.stderr)
        else:
            if median == self.last[2]: # newcomer goes in the middle
                self.knows = self.knows[:self.half+1]+[median]+self.knows[self.half+1:]
                self.search = None
                print ("Perfect hit! Learned something", self.knows, file=sys.stderr)
            elif median == self.last[1]: # newcomer is bigger, search right
                if self.last == (self.knows[-2], self.knows[-1], len(self.knows)+1):
                    self.knows.append(len(self.knows)+1)
                    self.search = None
                    print ("Rightmost element! Learned something", self.knows, file=sys.stderr)
                else:
                    self.search[0] = self.half
                    print ("Newcomer is bigger! Search right", self.search, file=sys.stderr)
            else: # newcomer is lower, search left
                if self.last == (self.knows[0], self.knows[1], len(self.knows)+1):
                    self.knows.insert(0, len(self.knows)+1)
                    self.search = None
                    print ("Leftmost element! Learned something", self.knows, file=sys.stderr)
                else:
                    self.search[1] = self.half
                    print ("Newcomer is lower! Search left", self.search, file=sys.stderr)
    def certain(self):
        return len(self.knows) == self.N
    def response(self):
        print ("Sending response", self.knows, "Queries", self.k, file=sys.stderr)
        return self.knows
    def log(self):
        for play, reply in zip(self.plays, self.replies):
            print (play, "->", reply, file=sys.stderr)

T, N, Q = map(int, input().split())
G = Guess(N, Q)
solved = 0
while T > 0:
    print (*G.query())
    median = int(input())
    if median == -1:
        print("Ran out of queries", file=sys.stderr)
        break
    G.update(median)
    if G.certain():
        G.log()
        print(*G.response())
        ok = int(input())
        if ok == -1:
            print("Wrong answer", file=sys.stderr)
            break
        G.reset()
        T -= 1
