# python3
from queue import Queue

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

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
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph, vertex_count, edge_count


def max_flow(graph:FlowGraph, from_:int, to:int):
    """
    Finds max flow within 'graph' with src 'from'
    and sink 'to' using Edmonds-Karp algorithm
    """
    prev = [0] * graph.size()
    prev[0] = (-1, -1, float('inf'))
    flow = 0
    while True:
        q = Queue()
        q.put(from_)
        marked = {from_}
        while to not in marked and not q.empty():
            node = q.get()
            for id in graph.get_ids(node):
                edge = graph.get_edge(id)
                if edge.capacity != 0 and edge.v not in marked:
                    marked.add(edge.v)
                    q.put(edge.v)
                    min_flow = min(prev[edge.u][2], edge.capacity)
                    # for this edge save it's id, prev node and curr min capacity
                    prev[edge.v] = (node, id, min_flow)
                    if to == edge.v:
                        # we find sink
                        break
        # if we reach sink
        if to in marked:
            flow += min_flow
            while node != - 1:
                # traverse back to src and decrease capacities of edges
                graph.edges[id].capacity -= min_flow
                graph.edges[id ^ 1].capacity -= (-min_flow)
                node, id, _ = prev[node]
        # if sink is not reachable
        else:
            break

    return flow
    

if __name__ == '__main__':
    graph, n, m = read_data()
    if n == 1 or m == 0:
        print(0)
    else:
        print(max_flow(graph, 0, graph.size() - 1))
