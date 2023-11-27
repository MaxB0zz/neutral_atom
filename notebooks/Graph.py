import networkx as nx
import matplotlib.pyplot as plt
from colors import Colors


class Graph:
    def __init__(self, problem_size):
        self.nodes = [i for i in range(1, problem_size + 1)]
        self.edges = []
        self.graph = None
        self.update_nx_graph()
        self.colors = {}

    def update_nx_graph(self):
        graph = nx.Graph()
        graph.add_nodes_from(self.nodes)
        graph.add_edges_from(self.edges)
        self.graph = graph

    def edd_edge(self, n1, n2):
        if n1 not in self.nodes and n2 not in self.nodes:
            print("ERROR: nodes not found")
        elif (n1, n2) in self.edges or (n2, n1) in self.edges:
            print("ERROR: edge already added")
        else:
            self.edges.append((n1, n2))

    def def_colors(self, bitstring):
        for idx, bit_string in enumerate(bitstring):
            for i, bit in enumerate(bit_string):
                if bit == '1':
                    self.colors[i + 1] = list(Colors)[idx].value

    def show_graph(self):
        pos = nx.spring_layout(self.graph)
        node_colors = [self.colors.get(node, 'lavender') for node in self.graph.nodes()]
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', node_size=2000, node_color=node_colors)
        nx.draw_networkx_edges(self.graph, pos)

        plt.title("Graph")
        plt.axis('off')
        plt.show()


bitstring = "0b1011"

g = Graph(5)
g.def_colors(bitstring)
g.show_graph()
print(list(Colors)[0].value)
