#!/usr/bin/python3

from concurrent.futures import process
import sys
import queue
from turtle import distance


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
        self.visited = [False] * n                 # visited[v] == True iff v was visited by forward or backward search
        self.workset = set()                          # All the nodes visited by forward or backward search
        # init nodes and it's indexes for bidir search
        self.nodes_forw = [[i, self.dist[0]] for i in range(n)]
        self.nodes_rev = [[i, self.dist[1]] for i in range(n)]
        self.proc = set()
        self.proc_r = set()


    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        # for v in self.workset:
        #     self.dist[0][v] = self.dist[1][v] = self.inf
        #     self.visited[v] = False

        # del self.workset[0:len(self.workset)]
        self.workset = set()
        self.nodes_forw = [[i, self.dist[0]] for i in range(n)]
        self.nodes_rev = [[i, self.dist[1]] for i in range(n)]
        self.proc = set()
        self.proc_r = set()
        

    def visit(self, q, side, v, dist):
        """Try to relax the distance to node v from direction side by value dist."""
        # Implement this method yourself


    def process_node(self, adj, cost, heap, proxy, u, dist, proc:set, size):
        # add this node to general processed set
        self.workset.add(u)
        for i, vert in enumerate(adj[u]):
            if dist[vert] > dist[u] + cost[u][i]:
                dist[vert] = dist[u] + cost[u]
                ChangePriority(heap, proxy[vert], dist[vert], proxy, size)
        proc.add(u)
    

    def shortest_path(self):
        # def min dist var
        distance = float('inf')
        # for every node in processed
        for u in self.workset:
            # check if dist to this node in 2 sides < distance
            if self.dist[0][u] + self.dist[1][u] < distance:
                distance = self.dist[0][u] + self.dist[1][u]
                
        return distance
    

    def query(self, adj, cost, s, t, n):
        n_forw = n_rev = n
        self.clear()
        # init dist to s and t nodes to 0
        self.dist[0][s], self.dist[1][t] = 0, 0
        self.nodes_forw[s], self.nodes_rev[t] = 0, 0
        # build heaps from nodes arrays 
        proxy_arr_forw, proxy_arr_rev = BuildHeap(self.nodes_forw, n), BuildHeap(self.nodes_rev, n)
        while n_forw or n_rev:
            """forward search"""
            u, n_forw = ExtractMin(self.nodes_forw, n_forw, proxy_arr_forw)
            # process exctracted node
            self.process_node(adj, cost, self.nodes_forw, proxy_arr_forw,
                              u, self.dist[0], self.proc, n_forw)
            # check if this node in another set
            if u in self.proc_r:
                return self.shortest_path()
            """backward search"""
            u, n_rev = ExtractMin(self.nodes_rev, n_rev, proxy_arr_rev)
            self.process_node(adj, cost, self.nodes_rev, proxy_arr_rev,
                              u, self.dist[1], self.proc_r, n_rev)
            if u in self.proc:
                return self.shortest_path()
        
        

        # q = [queue.PriorityQueue(), queue.PriorityQueue()]
        # self.visit(q, 0, s, 0)
        # self.visit(q, 1, t, 0)
        # Implement the rest of the algorithm yourself
        
        
        
        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u, v, c = readl()
        adj[0][u - 1].append(v - 1)
        cost[0][u-1].append(c)
        adj[1][v - 1].append(u - 1)
        cost[1][v - 1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s - 1, t - 1, n))
