#Uses python3

from math import floor
import re
import sys
from queue import Queue

def relax_edges(adj:list, cost:list, dist:list, prev:list):
    for u, reach in enumerate(adj):
        for j, v in enumerate(reach):
            if dist[v] > dist[u] + cost[u][j]:
                dist[v] = dist[u] + cost[u][j]
                prev[v] = u
                

def shortest_paths(adj, cost, s, distance, n):
    """Defines distance from node s
       to all other nodes"""
    # initialize dist array
    distance[s] = 0
    prev = [None] * n

    # use Bellman-Ford to relax edges
    for i in range(n - 1):
        relax_edges(adj, cost, distance, prev)

    neg_region = set()
    # find nodes reachable from negative cycle if any
    for i, u in enumerate(adj):
        for j, v in enumerate(u):
            if distance[v] > distance[i] + cost[i][j]:
                distance[v] = distance[i] + cost[i][j]
                neg_region.add(v)
                distance[v] = float('-inf')

    # BFS all nodes reachable from negative cycle
    q = Queue()
    [q.put(i) for i in neg_region]
    while not q.empty():
        vert = q.get()
        for v in adj[vert]:
            if v not in neg_region:
                q.put(v)
                distance[v] = float('-inf')
                neg_region.add(v)


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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    
    shortest_paths(adj, cost, s, distance, n)

    for x in range(n):
        if distance[x] == float('inf'):
            print('*')
        elif distance[x] == float('-inf'):
            print('-')
        else:
            print(distance[x])
