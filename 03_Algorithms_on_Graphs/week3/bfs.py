#Uses python3

import sys
from queue import Queue

def distance(adj, s, t, n):
    """Calculate distance in graph
       from 's' to 't' node
       with Breadth First Search"""
    dist = [float('inf')] * n # initialize inf for every dist
    dist[s] = 0               # def start node distance
    q = Queue()
    q.put(s)
    while not q.empty():
        vert = q.get()
        for v in adj[vert]:
            if dist[v] == float('inf'):
                q.put(v)
                dist[v] = dist[vert] + 1

    return -1 if dist[t] == float('inf') else dist[t]
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t, n))
