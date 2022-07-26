#!/usr/bin/python3

from random import randint
import sys

from queue import Queue
from math import sqrt, ceil
from heapq import heappop, heappush

class AStar:
    def __init__(self, n, adj, cost, x, y):
        # See the explanations of these fields in the starter for friend_suggestion        
        self.n = n
        self.adj = adj
        self.cost = cost
        self.inf = n * pow(10, 6)
        self.dist = {}
        self.visited = set()
        self.heap = []
        self.b_guess = {}
        self.x = x
        self.y = y

    # See the explanation of this method in the starter for friend_suggestion
    def clear(self):
        self.dist = {}
        self.visited = set()
        self.heap = []
        self.b_guess = {}


    def best_guess(self, n, t):
        """Calculates Euclidian dist btw 2 points"""
        return sqrt(pow(self.x[n] - self.x[t], 2) + pow(self.y[n] - self.y[t], 2))
        

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        """
        Finds the shortest path btw nodes 's' and 't'
        using A* algorithm
        """
        self.clear()
        # init starting vars
        self.dist[s] = 0
        self.b_guess[s] = self.best_guess(s, t)
        heappush(self.heap, (self.b_guess[s], s))

        while len(self.heap):
            b_guess, u = heappop(self.heap)
            self.visited.add(u)

            if u == t:
                return int(self.dist[u])

            # for every outgoing edge from node 'u'
            # find s.path to edge and approximate dist
            for i, vert in enumerate(self.adj[u]):
                path = self.dist[u] + self.cost[u][i]
                if path < self.dist.get(vert, self.inf):
                    self.dist[vert] = path
                    self.b_guess[vert] = path + self.best_guess(vert, t)
                    if vert not in self.visited:
                        heappush(self.heap, (self.b_guess[vert], vert))

        return -1

def best_dist(a, b, x:list, y:list):
        """Calculates Euclidian dist btw 2 points"""
        return ceil(sqrt(pow(x[a] - x[b], 2) + pow(y[a] - y[b], 2)))


def naive_dist(adj, cost, s, t, n):
    "Finds shortest path using BFS"
    dist = [float('inf') for _ in range(n)]
    # prev = [None for _ in range(n)]
    dist = [float('inf')] * n # initialize inf for every dist
    dist[s] = 0               # def start node distance
    q = Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                q.put(v)
                dist[v] = dist[u] + cost[u][i]

    return -1 if dist[t] == float('inf') else dist[t]


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u, v, c = readl()
        adj[u - 1].append(v - 1)
        cost[u - 1].append(c)
    t, = readl()
    astar = AStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        print(astar.query(s - 1, t - 1))


    # """Stress test functions"""
    # x = [-7, -4, -3, -6, 2, 3, 6, 3, -10, -2, -9, 3, 9, 8, 12, 13]
    # y = [-2, -5, 2, 6, 2, 6, 3, -5, 3, -2, -5, -9, -6, 7, 7, 2]
    # while True:
        
    #     # for _ in range(10):
    #     # n = randint(1, 100)
    #     # m =  randint(0, n * (n - 1))
    #     n = 16
    #     # m = 11
        
    #     m = randint(10, 20)
    #     edges = []
    #     E = set()

    #     while len(edges) != m:
            
    #         a = randint(1, n)
    #         b = randint(1, n)
    #         w = best_dist(a - 1, b - 1, x, y)
            
    #         if a != b and (a, b) not in E:
    #             E.add((a, b))
    #             t = ((a, b), w)                
    #             edges.append(t)

    #     s = t = 1
    #     while s == t:    
    #         s = randint(1, n)
    #         t = randint(1, n)
    #     # s, t = 2, 8

    #     # edges = [((8, 3), 2), ((7, 8), 2), ((12, 14), 5), ((5, 7), 4), ((8, 9), 3), ((2, 8), 5), ((6, 13), 3), ((14, 15), 1), ((16, 11), 4), ((1, 16), 4), ((2, 7), 1)]
    #     adj = [[] for _ in range(n)]
    #     cost = [[] for _ in range(n)]
    #     for ((a, b), w) in edges:
    #         adj[a - 1].append(b - 1)
    #         cost[a - 1].append(w)
          
        
    #     naive = naive_dist(adj, cost, s - 1, t - 1, n)
    #     astar = AStar(n, adj, cost, x, y)
    #     # try:
    #     #     bidir = bi_dijkstra.query(adj, cost, s, t, n)
    #     # except IndexError:
    #     #     print(n)
    #     #     for edge in edges:
    #     #         print(a, b, w)
    #     #     # print(edges)
    #     #     print(s, t)
    #     #     # print(E)
    #     #     break    
    #     path = astar.query(s - 1, t - 1)
    #     if naive != path:
    #         print("Naive:", naive)
    #         print("A*:", astar)
    #         print(n, m)
    #         for (i, j) in zip(x, y):
    #             print(i, j)
    #         for ((a, b), w) in edges:
    #             print(a, b, w)
    #         print(1)
    #         print(s, t)
    #         break
    #     else:
    #         print("OK!")
