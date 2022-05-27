#Uses python3

from operator import pos
import sys

sys.setrecursionlimit(200000)

visited = set()
post_counter = []
counter = 0

def dfs(adj, x):
    """Traverse the graph in DFS
       Input: adj. list graph, vertex number"""
    global visited, counter, post_counter
    #write your code here
    visited.add(x)
    counter += 1
    for vert in adj[x]:
        if vert not in visited:
            dfs(adj, vert)
    counter += 1
    post_counter.append((x, counter))
    return


def dfs_rev(adj, x):
    global visited
    #write your code here
    visited.add(x)
    for vert in adj[x]:
        if vert not in visited:
            dfs_rev(adj, vert)

    return


def number_of_strongly_connected_components(adj, adj_rev, n):
    """Count the number of SCC.
       Input: adj. list graph
       Output: number of SCC"""
    global post_counter
    result = 0
    # DFS graph and get post values for every vertex
    for vert in range(n):
        if vert not in visited:
            visited.add(vert)
            dfs(adj, vert)
    # sort post values in reverse order
    post_counter = sorted(post_counter, key=lambda x: x[1], reverse=True)
    visited.clear()

    # DFS reversed graph and count all SCC
    for vert in post_counter:
        vert = vert[0]
        if vert not in visited:
            dfs_rev(adj_rev, vert)
            result += 1

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # edges_rev = list(zip(data[1:(2 * m):2], data[0:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_rev = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_rev[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, adj_rev, n))
