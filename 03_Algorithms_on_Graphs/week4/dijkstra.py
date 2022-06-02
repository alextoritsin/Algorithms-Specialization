#Uses python3

import sys
from random import randint
from queue import Queue
import math

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


def distance(adj, cost, s, t, n):
    """Finds shortest path in graph
       from vert s to vert t using Dijkstra algorithm."""
    dist = [float('inf') for _ in range(n)]
    prev = [None for _ in range(n)]
    dist[s] = 0
    heap = [[i, dist[i]] for i in range(n)]
    proxy_arr = BuildHeap(heap, n)  # proxy_arr used to store indexes of elem in heap

    while n:
        u, n = ExtractMin(heap, n, proxy_arr)
      
        for i, vert in enumerate(adj[u]):
            if dist[vert] > dist[u] + cost[u][i]:  # change dist to vert if found smaller value
                dist[vert] = dist[u] + cost[u][i]
                prev[vert] = u
                ChangePriority(heap, proxy_arr[vert], dist[vert], proxy_arr, n)
             

    return -1 if dist[t] == float('inf') else dist[t]


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
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t, n))

    """Stress test functions"""

    # print(naive_dist(adj, cost, s, t, n))
    # print("Dijkstra:", distance(adj, cost, s, t, n))
    # print("Naive:", naive_dist(adj, cost, s, t, n))

    # while True:
    #     n = randint(1, 6)
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

    #     adj = [[] for _ in range(n)]
    #     cost = [[] for _ in range(n)]
    #     for ((a, b), w) in edges:
    #         adj[a - 1].append(b - 1)
    #         cost[a - 1].append(w)
        
    #     naive = naive_dist(adj, cost, s, t, n)

    #     try:
    #         dijkstra = distance(adj, cost, s, t, n)
    #     except TypeError:
    #         print(n)
    #         # for edge in edges:
    #         #     print(a, b, w)
    #         print(edges)
    #         print(s, t)
    #         # print(E)
    #         break    

    #     if naive != dijkstra:
    #         print("Naive:", naive)
    #         print("Dijkstra:", dijkstra)
    #         print(n, m)
    #         for ((a, b), w) in edges:
    #             print(a, b, w)
    #         print(s, t)
    #         break
    #     else:
    #         print("OK!")
