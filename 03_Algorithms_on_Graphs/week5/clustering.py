#Uses python3
import sys
import math


# cost = [[i, float('inf')] for i in range(n)]
#     parent = [None] * n
#     cost[0][1] = 0
#     proxy_arr = BuildHeap(cost, n)

#     nodes_left = set(range(n))
#     while n:
#         min_dist = float('inf')
#         vert, n = ExtractMin(cost, n, proxy_arr)
#         nodes_left = nodes_left - {vert}
#         for node in nodes_left:
#             d = distance(x[vert], x[node], y[vert], y[node])
#             if cost[proxy_arr[node]][1] > d:
#                 cost[proxy_arr[node]][1] = d
#                 if d < min_dist:
#                     min_dist = d
#                     ChangePriority(cost, proxy_arr[node], d, proxy_arr, n)
#         result += min_dist
            
#     return result


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
        parent[j_id] == i_id
    else:
        parent[i_id] == j_id
        # if rank are equal, increase i rank by 1
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1

def clustering(x, y, k):
    #write your code here
    return -1.


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
