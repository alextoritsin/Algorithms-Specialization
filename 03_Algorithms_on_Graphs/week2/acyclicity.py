#Uses python3

import sys

visited = set()

def reach(adj, vert):
    """Traverse the graph in DFS
       Return when same vertex met."""
    global visited

    for v in adj[vert]:
        if v not in visited:
            visited.add(v)
            reach(adj, v)
        else:
            return


def acyclic(adj, n):
    """Check if we have Directed Acyclic Graph"""
    global visited
    for vert in range(n):
        # For every vertex check if we have a loop from that vertex
        reach(adj, vert)

        if vert in visited:
            return 1
        else:
            visited.clear()
        
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj, n))
