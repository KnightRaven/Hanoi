#!/usr/bin/env python
import sys
class Hanoi():
    def __init__(self, n):
        self.n = n
        self.bar = []
        for i in range(3):
            self.bar.append([])             # Create 3 bars.
        self.bar[0] = range(n)              # Fill the first bar with plates in order.
        for i in range(n):
            self.bar[1].append(None)
            self.bar[2].append(None)        # Fill the next two bars with None.
        self.dic = {0:'A', 1:'B', 2:'C'}    # Create a dic to map figures and bars.

    def move(self, n, a=0, b=2):
        for i in range(3):
            if i not in [a,b]:
                c = i
        if n == 1:
            self.movesingle(n, a, b)
        else:
            self.move(n-1, a=a, b=c)
            self.movesingle(n, a, b)
            self.move(n-1, a=c, b=b)

    def movesingle(self, n, a, b):
        self.bar[b][n-1] = self.bar[a][n-1]
        self.bar[a][n-1] = None
        print "No.{0} from {1} to {2}".format(n, self.dic[a], self.dic[b])

    def solute(self):
        self.move(self.n)

if __name__ == "__main__":
    hanoi = Hanoi(int(sys.argv[1]))
    hanoi.solute()
