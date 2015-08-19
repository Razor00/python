#!/usr/bin/python
from __future__ import print_function

        
class MAZE:
    (top, left, right, bottom) = (0, 1, 2, 3)
    def __init__(self, m, n):
        self.rows = m
        self.cols = n
        self.N = m * n
        N = m * n
        self.root = [i for i in range(N)]
        self.rank = [0] * N
        self.count = N
        self.walls =[[True]*4 for i in range(N)] #four walls for each room
        self.nbr_offset = [-n, -1, 1, n] 

    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]

    def display(self):
        printf(self.root)
        printf(self.rank)

    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)

        # i, j are already connected
        if rooti == rootj:
            return
        
        self.count -= 1

        if self.rank[rooti] == self.rank[rootj]:
            self.root[rootj] = self.root[rooti]
            self.rank[rooti] +=1
            return

        # when both the trees are of equal height 
        if self.rank[rooti] > self.rank[rootj]:
            self.root[rootj] = self.root[rooti];
        else:
            self.root[rooti] = self.root[rootj];
        return

    def get_count(self):
        return self.count


    def is_connected(self):
        return self.get_count() == 1

    def connected(self, i, j):
        return self.find(i) == self.find(j)

    def valid_neighbor(self, nbr, dir):
        if MAZE.top == dir:
            return nbr >= 0

        if MAZE.bottom == dir:
            return nbr < self.N

        if MAZE.left == dir:
            return (nbr+1) % self.cols != 0

        if MAZE.right == dir:
            return nbr % self.cols != 0


    def get_neighbor(self, room, dir):
        return (room + self.nbr_offset[dir])

    def is_wall_closed(self, room, dir):
        return self.walls[room][dir]    

    def wall_remove(self, room, dir):
        self.walls[room][dir] = False
    
    def hastop(self, room):
        return self.walls[room][MAZE.top]

    def hasleft(self, room):
        return self.walls[room][MAZE.left]

    def hasright(self, room):
        return self.walls[room][MAZE.right]

    def hasbottom(self, room):
        return self.walls[room][MAZE.bottom]

    def print_maze(self):
        v = 0
        for i in range(self.rows):
            k = v
            for j in range(self.cols):
                print("+", end='')
                if self.hastop(k):
                    print("---", end='')
                else:
                    print("   ", end='')
                k += 1
            k = v
            print("+")
            for j in range(self.cols):
                if self.hasleft(k):
                    print("|   ", end='') #print "| %-3d " % k,
                else:
                    print("    ", end='') #print "  %-3d " % k, 
                k += 1

            if self.hasright(k-1):
                print("|", end='')

            print("")
            v += self.cols
        k = v-self.cols
        for j in range(self.cols):
            print("+", end = '')
            if self.hasbottom(k):
                print("---", end='')
            else:
                print("   ", end='')
 
        print("+")
"""
    def print_maze1(self):
        v = 0
        print " --- "* (self.rows+1)
        for i in range(self.rows):
            for j in range(self.cols):
                print"| %-2d" % v,
                v +=1
            print "|"
            print " --- "* (self.rows+1)
    
"""
import random as r


m = int(raw_input("Enter the number of rows of maze: "))
n = int(raw_input("Enter the number of columnns of maze: "))
N = m * n
maze = MAZE(m, n)


while not maze.is_connected():
    room = r.randrange(0, N) 
    dir  = r.randrange(0, 4)
    nbr  = maze.get_neighbor(room, dir)
    if maze.is_wall_closed(room, dir) and maze.valid_neighbor(nbr, dir) and not maze.connected(room, nbr):
        maze.union(room, nbr)
        maze.wall_remove(room, dir)
        maze.wall_remove(nbr, 3-dir) 
        

maze.print_maze()

"""
uf.display()
raw_input("Press Enter")
uf.union(0,3)

uf.display()
raw_input("Press Enter")
uf.union(1,2)

uf.display()
raw_input("Press Enter")
uf.union(5,6)

uf.display()
raw_input("Press Enter")
uf.union(6,7)

uf.display()
raw_input("Press Enter")
uf.union(0,2)

uf.display()
raw_input("Press Enter")
uf.union(3,7)

uf.display()
raw_input("Press Enter")
uf.union(0,5)
uf.display()
"""

