# python3
from queue import Queue

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity


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


class StockCharts:

    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for i in range(n)]
        # create graph with edges from s to 'n' first nodes
        graph = FlowGraph(n * 2 + 2)
        return stock_data, graph, n


    def draw_path(self, graph:FlowGraph, start_nodes, sink_nodes, end):
        """Draws edges from source and to sink"""
        for node in start_nodes:
            graph.add_edge(0, node, 1)
        
        for node in sink_nodes:
            graph.add_edge(node, end, 1)

        return graph


    def construct_graph(self, stock_data:list, graph:FlowGraph, n:list):
        """
        Constructs bipartite graph based on stock data:
        for every two stocks i and j add edge in graph
        from i to j if every point of stock i is less than
        every point of stock j; otherwise — add edge from j to i.
        """
        sink_nodes = set()
        start_nodes = set()
        end_node = n * 2 + 1
        for i, stock in enumerate(stock_data):
            for j in range(i + 1, len(stock_data)):
                if stock_data[i][0] != stock_data[j][0]:
                    # get invariant
                    invar = stock_data[i][0] < stock_data[j][0]
                    # compare following points
                    for k in range(1, len(stock)):
                        p1, p2 = stock_data[i][k], stock_data[j][k]
                        if (p1 == p2) or ((p1 < p2) != invar): 
                            # invariant broke
                            break
                    # processed all points 
                    else:
                        if invar:
                            # add edge from i to j
                            graph.add_edge(i + 1, j + n + 1, 1)
                            start_nodes.add(i + 1)
                            sink_nodes.add(j + n + 1)
                        else:
                            # add edge from j to i
                            graph.add_edge(j + 1, i + n + 1, 1)
                            start_nodes.add(j + 1)
                            sink_nodes.add(i + n + 1)
    
        # add start and sink nodes
        graph = self.draw_path(graph, start_nodes, sink_nodes, end_node)

        return graph


    def max_flow(self, graph:FlowGraph, end:int):
        """
        Calculates max flow in bipartite graph
        """
        prev = [0] * graph.size()
        prev[0] = (-1, -1)
        flow = 0
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
                flow += 1
                while node != - 1:
                    # traverse back to src and decrease capacities of edges
                    graph.edges[id].capacity -= 1
                    graph.edges[id ^ 1].capacity -= (-1)
                    node, id = prev[node]
            else:
                break

        return flow
        

    def solve(self):
        stock_data, graph, n = self.read_data()
        graph = self.construct_graph(stock_data, graph, n)
        # printing the minimum number of non-overlaping charts
        print(n - self.max_flow(graph, n * 2 + 1))
        

if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()
