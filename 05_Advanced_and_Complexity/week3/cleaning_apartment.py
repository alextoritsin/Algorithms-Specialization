# python3
import itertools
from math import factorial

def ham_to_SAT(n, e_count, edges):
    # compute number of variables and clauses
    max_edges = n * (n - 1) // 2
    non_adj_edges = max_edges - e_count
    combs = factorial(n) // (factorial(n - 2) * 2)
    clauses = n * 2 + n * 2 * combs + non_adj_edges * (n - 1) * 2
    vars = pow(n, 2)

    # calc possible positions of each vertex
    # where pos[i][j] — (i+1)-th position of Hamilton path
    # occupied by node j - n * i
    pos = [0] * n
    for i in range(n):
        pos[i] = list(range(i * n + 1, i * n + 1 + n))

    # print number of clauses and varirables
    print(clauses, vars)

    # each node j must appear in the path
    for j in range(n):
        print(" ".join([str(pos[i][j]) for i in range(n)]), "0")

    # no node appears twice in the path
    for j in range(n):
        for comb in itertools.combinations([pos[k][j] for k in range(n)], 2):
            print(" ".join([str(-p) for p in comb]), "0")

    # every position i must be occupied
    for i in range(n):
        print(" ".join([str(j) for j in pos[i]]), "0")
    
    # no two nodes occupy the same position
    for i in range(n):
        for comb in itertools.combinations(pos[i], 2):
            print(" ".join([str(-p) for p in comb]), "0")

    # nonadjacent nodes cannot be adjacent in the path
    for edge in itertools.combinations(range(n), 2):
        i, j = edge
        if not edges[i][j]:
            for k in range(n - 1):
                print(-pos[k][i], -pos[k + 1][j], 0)
                print(-pos[k][j], -pos[k + 1][i], 0)



if __name__ == '__main__':
    # graph input
    n, m = list(map(int, input().split()))
    edges_d = dict()
    edges = [[0] * n for i in range(n)]
    e_count = 0
    for i in range(m):
        a, b = map(int, input().split())
        if not edges[a - 1][b - 1]:
            e_count += 1
            edges[a - 1][b - 1], edges[b - 1][a - 1] = 1, 1

    if m == 0:
        if n < 2:
            # Hamilton path is always exists in graph of 1 vertex
            print(1, 1)
            print(1, -1, 0)
        else:
            # graph is not connected for sure
            print(2, 1)
            print(1, 0)
            print(-1, 0)
    else:
        ham_to_SAT(n, e_count, edges)

        


