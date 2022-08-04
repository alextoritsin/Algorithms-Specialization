# python3
from queue import Queue
from random import randint

# from sonia_exp import MakeNetwork, MaxFlow, HasPath

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]


def read_data():
    n, m = map(int, input().split())
    graph = FlowGraph(n + m + 2)
    for i in range(n):
        graph.add_edge(0, i + 1, 1)
    
    for i in range(n):
        crew = list(map(int, input().split()))
        for j, ready in enumerate(crew):
            if ready == 1:
                graph.add_edge(i + 1, j + n + 1, 1)
    
    for i in range(n + 1, n + m + 1):
        graph.add_edge(i, n + m + 1, 1)

    return graph, n, m


def max_flow(graph:FlowGraph, n:int, end:int):
    """
    Finds matches in bipartite graph of sets
    'n' and 'm' verteces
    """
    prev = [0] * graph.size()
    next = [0] * graph.size()
    prev[0] = (-1, -1)
    while True:
        q = Queue()
        q.put(0)
        marked = {0}
        while end not in marked and not q.empty():
            node = q.get()
            for id in graph.get_ids(node):
                edge = graph.get_edge(id)
                if edge.capacity != 0 and edge.v not in marked:
                    marked.add(edge.v)
                    q.put(edge.v)
                    prev[edge.v] = (node, id)
                    if edge.v == end:
                        break
        
        if end in marked:
            while node != - 1:
                # save node ids for later matching
                next[node] = graph.get_edge(id).v
                # traverse back to src and decrease capacities of edges
                graph.edges[id].capacity -= 1
                graph.edges[id ^ 1].capacity -= (-1)
                node, id = prev[node]
        else:
            break

    return " ".join([str(-1) if next[i] == 0 else str(next[i] - n) for i in range(1, 1 + n)])
    

if __name__ == '__main__':
    graph, n, m = read_data()
    print(max_flow(graph, n, n + m + 1))


    """stress testing"""
    # n = randint(3, 4)
    # m = randint(3, 4)
    # bipartite = [[0] * m for _ in range(n)]
    # for i in range(n):
    #     for j in range(m):
    #         bipartite[i][j] = randint(0, 1)


    # graph = read(bipartite, n, m)
    # my_ans = max_flow(graph, n, n + m + 1)

    # print(n, m)
    # for i in range(n):
    #     print(" ".join([str(j) for j in bipartite[i]]))
    # print(my_ans)
    


