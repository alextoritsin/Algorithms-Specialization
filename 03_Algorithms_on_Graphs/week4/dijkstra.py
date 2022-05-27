#Uses python3

import sys
from collections import deque


def BuildHeap(array:deque, size):
    
    for i in range(size // 2, -1):
        SiftDown(i)

def SiftDown(array:deque, i, size):
    minindex = i
    l = LeftChild(i)
    if l <= size and array[l] < array[i]:
        minindex = l
    r = RightChild(i)
    if r <= size and array[r] < array[i]:
        minindex = r
    if i != minindex:
        array[i], array[minindex] = array[minindex], array[i]


def SiftUp(array, i):
    parent = (i - 1) // 2
    while i > 0 and array[parent] > array[i]:
        parent = (i - 1) // 2
        array[parent], array[i] = array[i], array[parent]
        i = parent


def ChangePriority(array, i, value):
    oldp = array[i]
    array[i] = value
    if value > oldp:
        SiftDown(array, i, len(array))
    else:
        SiftUp(array, i)


def ExtractMin(array:deque, size):
    result = array[0]
    array[0] = array[size - 1]
    size = size - 1
    SiftDown(array, 0, size)
    return result, size


def LeftChild(i):
    return 2 * i + 1
    

def RightChild(i):
    return 2 * i + 2


def distance(adj, cost, s, t, n):
    dist = [float('inf') for u in range(n)]
    prev = [None for u in range(n)]
    dist[0] = 0
    heap = deque(dist)
    # BuildHeap(heap, n)
    
    while n:
        u, n = ExtractMin(heap, n)
        for i, vert in enumerate(adj[u]):
            if dist[vert] > dist[u] + cost[u][i]:
                dist[vert] = dist[u] + cost[u][i]
                prev[vert] = u
                ChangePriority(heap, vert, dist[vert])                
                
    return dist[t] - dist[s]


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
