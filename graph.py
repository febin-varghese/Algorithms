# Creating a graph using adjacency list
"""
0-----1
|    /|\
|  /  | 2
|/    |/
4-----3
"""


class AdjNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node {self.value}"


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * vertices

    def add_edge(self, src: int, des: int):
        node = AdjNode(des)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[des]
        self.graph[des] = node

    def print_graph(self):
        print("Adjacency lists of the graph:")
        for i in range(self.vertices):
            print(i, end="")
            node = self.graph[i]
            while node:
                print(f" -> {node.value}", end="")
                node = node.next
            print("\n")

    def __repr__(self):
        return f"Graph of {self.vertices} vertices (nodes)"


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph_edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
    for n in graph_edges:
        graph.add_edge(n[0], n[1])
    graph.print_graph()
