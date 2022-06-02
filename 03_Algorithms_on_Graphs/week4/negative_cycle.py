#Uses python3

import sys

def relax_edges(adj:list, cost:list, dist:list):
    for i, u in enumerate(adj):
        for j, v in enumerate(u):
            if dist[v] > dist[i] + cost[i][j]:
                dist[v] = dist[i] + cost[i][j]
    


def negative_cycle(adj, cost, n):
    """Checks for negative cycle in graph
       using Bellman-Ford algorithm"""
    # for every start vertex check if we have negative cycle
    for vert in range(n):
        # initialize dist array
        dist = [float('inf')] * n
        dist[vert] = 0               
        # relax edges while something changes or
        # number of iterations less or equal to num. of vert
        ok = False
        count = 0
        while not ok and count <= n:

            ok = True
            for i, u in enumerate(adj):
                for j, v in enumerate(u):
                    if dist[v] > dist[i] + cost[i][j]:
                        dist[v] = dist[i] + cost[i][j]
                        ok = False                        
            count += 1

        # if iterations more than vert - we have a neg. cycle.
        if count > n:
            return 1
    
    return 0


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
    print(negative_cycle(adj, cost, n))
