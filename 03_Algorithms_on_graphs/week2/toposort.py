#Uses python3

import sys

used = set()
order = []

def reach(adj, vert):
    """Traverse graph in DFS.
    Stops at sink and add it 
    to the order array"""
    global used

    for v in adj[vert]:
        if v not in used:
            reach(adj, v)

    used.add(vert)
    order.append(vert + 1)


def toposort(adj, n):
    """Input: adjicency list graph
       Output: topologically sorted array"""
    global used, order

    for vert in range(n):
        if vert not in used:
            reach(adj, vert)
    # output in reverse order
    print(" ".join([str(order[x]) for x in range(-1, -(n + 1), -1)]))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    toposort(adj, n)
