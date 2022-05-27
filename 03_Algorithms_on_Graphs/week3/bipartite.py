#Uses python3

import sys
from queue import Queue

def bipartite(adj, n):
    """Check if a graph is bipartite,
       i.e. each edge have vertexes
       of different color"""
    colors = [None] * n # initialize inf for every colors
    q = Queue()
    for vert in range(n):
        if not colors[vert]:
            colors[vert] = 1      # def start node color
            q.put(vert)
            
            while not q.empty():
                # put vertex in the queue
                vert = q.get()
                # for every v from this vertex check dif values
                for v in adj[vert]:
                    if not colors[v]: # vertex not visited before
                        q.put(v)
                        colors[v] = 2 if colors[vert] == 1 else 1
                    elif colors[v] == colors[vert]:  # vertexes have same color
                        return 0
                        
    return 1


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
    print(bipartite(adj, n))
