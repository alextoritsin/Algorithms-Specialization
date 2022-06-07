#Uses python3
import sys
import math


def Union(i, j, parent:list, rank:list):
    """Unites two sets i and j using
       union by rank heuristic"""
    # find the parents of elem. i and j
    i_id = Find(i, parent)
    j_id = Find(j, parent)

    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        # if rank are equal, increase i rank by 1
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1



def Find(i, parent:list):
    """Finds parent of element i
       with path compression heuristic"""
    if i != parent[i]:
        # attach elem. i and all elem. on the path directly to the root
        parent[i] = Find(parent[i], parent)
    return parent[i]


def distance(x1, x2, y1, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def minimum_distance(x, y, n):
    """Calculate min distance of minimun
       spanning tree of n nodes
       (points with x and y coords)
       using Kruskal algorithm"""
    result = 0
    parent = list(range(n))
    rank = [0] * n
    nodes = set(range(n))
    processed = set()
    edges = [0] * ((n * (n - 1)) // 2) if n > 1 else [0]
    k = 0
    # get all posible edges
    for i in range(n):
        for j in (nodes - {i} - processed):
            edges[k] = ((i, j), distance(x[i], x[j], y[i], y[j]))
            k += 1

        processed.add(i)

    if n == 1:
        return result
    elif n == 2:
        return edges[0][1]
    else:
        # sort edges in increasing order
        edges.sort(key=lambda x: x[1])


    for ((u, v), dist) in edges:
        if Find(u, parent) != Find(v, parent):
            result += dist
            Union(u, v, parent, rank)
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y, n)))
