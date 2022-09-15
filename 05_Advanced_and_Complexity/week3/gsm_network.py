# python3

def print_CNF(edges, n):
    """
    Converts graph coloring problem to 3-SAT problem
    with formula in CNF. Prints all clauses of this form
    """
    vars = [0] * n
    vars = [tuple(range(3 * v + 1, 3 * v + 4)) for v in range(n)]

    # print num of clauses and variables
    print(n + len(edges) * 3, n * 3)

    # print all vertex constraints
    # every vertex must have only 1 color
    for clause in vars:
        print(" ".join([str(c) for c in clause]), "0")

    # print all edges constraits
    # every edge must have different endpoints colors
    for edge in edges:
        u, v = edge[0] - 1, edge[1] - 1
        for k in range(3):
            print(-vars[u][k], -vars[v][k], 0)



if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]
    print_CNF(edges, n)


