#Uses python3
import sys
import math



def Find(i, parent:list):
    """Finds parent of element i
       with pass compression heuristic"""
    if i != parent[i]:
        # attach elem. i and all elem. on the path directly to the root
        parent[i] = Find(parent[i], parent)
    return parent[i]
    

def Union(i, j, parent:list, rank:list):
    """Unites two sets i and j using
       union by rank heuristic"""
    # find the parents of elem. i and j
    i_id = Find(i, parent)
    j_id = Find(j, parent)
    # i and j are elements of the same set
    if i_id == j_id:
        return

    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        # if rank are equal, increase i rank by 1
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1


def distance(x1, x2, y1, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
            

def clustering(x, y, k, n):
    """Computes the minimum distance
       between k clasters of n points
       using Kruskal algorithm"""
    parent = list(range(n))
    rank = [0] * n
    nodes = set(range(n))
    processed = set() 
    edges = [0] * ((n * (n - 1)) // 2) if n > 1 else [0]
    edge = 0

    # get all posible edges
    for i in range(n):
        for j in (nodes - {i} - processed):
            edges[edge] = ((i, j), distance(x[i], x[j], y[i], y[j]))
            edge += 1

        processed.add(i)

    if n == 2:
        return edges[0][1]
    else:
        edges.sort(key=lambda x: x[1])
        if n == k:
            return edges[0][1]
        else:
            i = 0
            # go throught all edges until having k clasters
            while n >= k:
                ((u, v), dist) = edges[i]
                if Find(u, parent) != Find(v, parent):
                    # union sets to decrease num. of clasters
                    Union(u, v, parent, rank)
                    n -= 1
                i += 1

            return dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k, n)))
