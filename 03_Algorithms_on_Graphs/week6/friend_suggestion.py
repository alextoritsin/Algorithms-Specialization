#!/usr/bin/python3

import sys
from queue import Queue
from random import randint

def BuildHeap(array, size):
    """Builds binary heap from array
       Returns proxy array to store
       indexes of items in heap"""
    proxy_arr = list(range(size))
    for i in range(size // 2, -1, -1):
        SiftDown(array, i, size, proxy_arr)
    return proxy_arr


def SiftDown(array:list, i, size, proxy_arr:list):
    """Pushes element of heap to bottom"""
    if 2 * i + 1 >= size:
        return

    minindex = i
    left, right = 2 * i + 1, 2 * i + 2  # find left and right childs

    if left < size and array[left][1] < array[minindex][1]:
        minindex = left

    if right < size and array[right][1] < array[minindex][1]:
        minindex = right

    if i != minindex:
        # get the nodes we about to change 
        p_min, p_i = array[minindex][0], array[i][0]
        # swap nodes in heap
        array[i], array[minindex] = array[minindex], array[i]
        # swap indexes of nodes to track
        proxy_arr[p_i], proxy_arr[p_min] = proxy_arr[p_min], proxy_arr[p_i]
        SiftDown(array, minindex, size, proxy_arr)


def SiftUp(array, i, proxy_arr:list):
    """Pushes element of heap to top"""
    while i > 0 and array[Parent(i)][1] > array[i][1]:
        # get the nodes we're about to change
        p_node, i_node = array[Parent(i)][0], array[i][0]
        # swap nodes in heap
        array[Parent(i)], array[i] = array[i], array[Parent(i)]
        # swap indexes of nodes to track
        proxy_arr[p_node], proxy_arr[i_node] = proxy_arr[i_node], proxy_arr[p_node]
        i = Parent(i)


def Parent(i):
    return (i - 1) // 2


def ChangePriority(array, i, value, proxy_arr, size):
    """Changes value of item in heap"""
    oldp = array[i][1]
    array[i][1] = value
    if value > oldp:
        SiftDown(array, i, size, proxy_arr)
    else:
        SiftUp(array, i, proxy_arr)


def ExtractMin(array:list, size, proxy_arr:list):
    """Extract vertex with min value from heap"""
    # get min node in heap
    min_node = array[0][0]
    # replace first node in heap with last
    array[0] = array[size - 1]
    # set index of the last node to 0
    proxy_arr[array[size - 1][0]] = 0
    # show that extracted node haven't in heap
    proxy_arr[min_node] = None
    size = size - 1
    array.pop()
    SiftDown(array, 0, size, proxy_arr)
    return min_node, size


class BiDij:
    def __init__(self, n):
        self.n = n;                                # Number of nodes
        self.inf = n * 10 ** 6                     # All distances in the graph are smaller
        self.dist = [[self.inf] * n, [self.inf] * n]  # Initialize distances for forward and backward searches

        self.workset = set()                          # All the nodes visited by forward or backward search
        # init nodes and it's indexes for bidir search
        self.nodes_forw = [[i, self.dist[0][i]] for i in range(n)]
        self.nodes_rev = [[i, self.dist[1][i]] for i in range(n)]
        self.proc = set()
        self.proc_r = set()


    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        self.workset = set()
        self.proc = set()
        self.proc_r = set()
        self.dist = [[self.inf] * n, [self.inf] * n]
        self.nodes_forw = [[i, self.dist[0][i]] for i in range(n)]
        self.nodes_rev = [[i, self.dist[1][i]] for i in range(n)]
        

    def process_node(self, adj, cost, heap, proxy, u, dist, proc:set, size):
        """Relax nodes outcoming from u and change thier priority"""
        # add this node to general processed set
        self.workset.add(u)
        for i, vert in enumerate(adj[u]):
            if dist[vert] > dist[u] + cost[u][i]:
                dist[vert] = dist[u] + cost[u][i]
                ChangePriority(heap, proxy[vert], dist[vert], proxy, size)
        proc.add(u)
    

    def shortest_path(self):
        """Define s.path based on processed nodes"""
        # def min dist var
        distance = float('inf')
        # for every node in processed
        for u in self.workset:
            # check if dist to this node in sum of 2 sides less than distance
            if self.dist[0][u] + self.dist[1][u] < distance:
                distance = self.dist[0][u] + self.dist[1][u]
                
        return distance
    

    def query(self, adj, cost, s, t, n):
        n_forw = n_rev = n
        self.clear()
        # init dist to s and t nodes to 0
        self.dist[0][s], self.dist[1][t] = 0, 0
        self.nodes_forw[s][1], self.nodes_rev[t][1] = 0, 0
        # build heaps from nodes arrays 
        proxy_arr_forw, proxy_arr_rev = BuildHeap(self.nodes_forw, n), BuildHeap(self.nodes_rev, n)
        # loop until all nodes proccessed
        while n_forw or n_rev:
            # check whether all posib. nodes relaxed
            if self.nodes_forw[0][1] == self.nodes_rev[0][1] == self.inf:
                break
            else:
                """forward search"""
                # extract only relaxed node
                if self.nodes_forw[0][1] != self.inf:
                    u, n_forw = ExtractMin(self.nodes_forw, n_forw, proxy_arr_forw)
                    # process exctracted node
                    self.process_node(adj[0], cost[0], self.nodes_forw, proxy_arr_forw,
                                    u, self.dist[0], self.proc, n_forw)
                    # check if this node in another set
                    if u in self.proc_r:
                        return self.shortest_path()

                """backward search"""
                # extract only relaxed node
                if self.nodes_rev[0][1] != self.inf:
                    u, n_rev = ExtractMin(self.nodes_rev, n_rev, proxy_arr_rev)
                    self.process_node(adj[1], cost[1], self.nodes_rev, proxy_arr_rev,
                                    u, self.dist[1], self.proc_r, n_rev)
                    if u in self.proc:
                        return self.shortest_path()

        return -1


def readl():
    return map(int, sys.stdin.readline().split())


def naive_dist(adj, cost, s, t, n):
    "Finds shortest path using BFS"
    dist = [float('inf') for _ in range(n)]
    prev = [None for _ in range(n)]
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
    #     n = randint(1, 100)
    #     m =  randint(0, n * (n - 1))
    #     # n = 10
    #     # m = 7
    #     edges = []
    #     E = set()

    #     while len(edges) != m:
    #         w = randint(0, 5)
            
    #         a = randint(1, n)
    #         b = randint(1, n)
            
    #         if a != b and (a, b) not in E:
    #             E.add((a, b))
    #             t = ((a, b), w)                
    #             edges.append(t)


    #     s = randint(1, n) - 1
    #     t = randint(1, n) - 1
    #     # s, t = 5, 1

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
    #     except TypeError:
    #         print(n)
    #         # for edge in edges:
    #         #     print(a, b, w)
    #         print(edges)
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