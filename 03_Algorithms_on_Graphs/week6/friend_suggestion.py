#!/usr/bin/python3

import sys
from queue import Queue
from heapq import heappush, heappop
from random import randint



class BiDij:
    def __init__(self, n):
        self.dist = {'forw': {}, 'back': {}}
        self.n = n;                                # Number of nodes
        self.inf = n * pow(10, 6)                    # All distances in the graph are smaller

        # init nodes and it's indexes for bidir search
        self.heap = {'forw': [], 'back': []}
        self.visited = {'forw': set(), 'back': set()}


    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        self.visited = {'forw': set(), 'back': set()}
        self.heap = {'forw': [], 'back': []}
        self.dist = {'forw': {}, 'back': {}}

        
    def relax(self, adj:list, cost, heap:list, dist:dict, u, mu, side):
        for i, vert in enumerate(adj[u]):
            if dist.get(vert, self.inf) > dist[u] + cost[u][i]:
                dist[vert] = dist[u] + cost[u][i]
                heappush(heap, (dist[vert], vert))

            if vert in self.visited[side] and dist[u] + cost[u][i] + self.dist[side].get(vert, self.inf) < mu:
                mu = dist[u] + cost[u][i] + self.dist[side][vert]

        return mu


    def query(self, adj, cost, s, t, n):
        n_forw = n_rev = n
        self.clear()
        # init dist to s and t nodes to 0
        self.dist['forw'][s] = 0
        self.dist['back'][t] = 0

        heappush(self.heap['forw'], (0, s))
        heappush(self.heap['back'], (0, t))
        mu = self.inf
        while len(self.heap['forw']) and len(self.heap['back']):
            node_f, u = heappop(self.heap['forw'])
            while u in self.visited['forw']:
                if len(self.heap['forw']) == 0:
                    break
                node_f, u = heappop(self.heap['forw'])
                 
            node_b, v = heappop(self.heap['back'])
            while v in self.visited['back']:
                if len(self.heap['back']) == 0:
                    break
                node_f, v = heappop(self.heap['back'])

            self.visited['forw'].add(u)
            self.visited['back'].add(v)
            
            mu = self.relax(adj[0], cost[0], self.heap['forw'], self.dist['forw'], u, mu, 'back')
            mu = self.relax(adj[1], cost[1], self.heap['back'], self.dist['back'], v, mu, 'forw')

            if self.dist['forw'].get(u, self.inf) + self.dist['back'].get(v, self.inf) >= mu:
                break

        return -1 if mu == self.inf else mu    
            

def readl():
    return map(int, sys.stdin.readline().split())


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


if __name__ == '__main__':
    n, m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u, v, c = readl()
        adj[0][u - 1].append(v - 1)
        cost[0][u - 1].append(c)
        adj[1][v - 1].append(u - 1)
        cost[1][v - 1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        if s == t:
            print(0)
        else:
            print(bidij.query(adj, cost, s - 1, t - 1, n))


    # """Stress test functions"""

    # while True:
    # # for _ in range(10):
    #     # n = randint(1, 100)
    #     # m =  randint(0, n * (n - 1))
    #     n = 10
    #     m = 7
    #     # edges = [((6, 5), 1), ((6, 1), 3), ((1, 6), 4), ((9, 3), 1), ((7, 9), 2), ((5, 2), 2), ((7, 3), 4)]
    #     edges = []
    #     E = set()

    #     while len(edges) != m:
    #         w = randint(1, 5)
            
    #         a = randint(1, n)
    #         b = randint(1, n)
            
    #         if a != b and (a, b) not in E:
    #             E.add((a, b))
    #             t = ((a, b), w)                
    #             edges.append(t)


    #     s = t = 1
    #     while s == t:    
    #         s = randint(1, n) - 1
    #         t = randint(1, n) - 1
    #     # s, t = 5, 0

    #     adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    #     cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    #     for ((a, b), w) in edges:
    #         adj[0][a - 1].append(b - 1)
    #         cost[0][a - 1].append(w)
    #         adj[1][b - 1].append(a - 1)
    #         cost[1][b - 1].append(w)
        
    #     naive = naive_dist(adj[0], cost[0], s, t, n)
    #     bi_dijkstra = BiDij(n)
    #     # bidir = bi_dijkstra.query(adj, cost, s, t, n)
    #     try:
    #         bidir = bi_dijkstra.query(adj, cost, s, t, n)
    #     except IndexError:
    #         print(n)
    #         for edge in edges:
    #             print(a, b, w)
    #         # print(edges)
    #         print(s, t)
    #         # print(E)
    #         break    

    #     if naive != bidir:
    #         print("Naive:", naive)
    #         print("Dijkstra:", bidir)
    #         print(n, m)
    #         for ((a, b), w) in edges:
    #             print(a, b, w)
    #         print(s, t)
    #         break
    #     else:
    #         print("OK!")