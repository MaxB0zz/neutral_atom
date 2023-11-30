import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from colors import Colors


class Graph:
    def __init__(self, antenna_coordinates, interference_threshold=8.7):
        self.nodes = [i for i in range(1, len(antenna_coordinates) + 1)]
        self.edges = []
        self.coordintes = antenna_coordinates
        self.graph = None
        self.color = 0
        self.update_nx_graph()
        N = len(antenna_coordinates)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                antenna_i = np.array([coord for coord in antenna_coordinates[i]])
                antenna_j = np.array([coord for coord in antenna_coordinates[j]])
                dist = np.linalg.norm(antenna_j - antenna_i)
                if dist < interference_threshold:
                    self.add_edge(i + 1, j + 1)

        self.colors = {}

    def update_nx_graph(self):
        graph = nx.Graph()
        graph.add_nodes_from(self.nodes)
        graph.add_edges_from(self.edges)
        self.graph = graph

    def add_edge(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes and (n1, n2) not in self.edges and (n2, n1) not in self.edges:
            self.edges.append((n1, n2))
            self.graph.add_edge(n1, n2)

    def def_colors(self, bitstring):
        for i in range(len(bitstring)):
            if bitstring[i] == '1':
                self.colors[i + 1] = list(Colors)[self.color].value
        self.color += 1
        return self.return_uncolored_graph()

    def show_graph(self, pos):
        node_colors = [self.colors.get(node, 'lavender') for node in self.graph.nodes()]
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', node_color=node_colors, font_color='black', font_size=8)
        plt.figure(1)
        plt.title("Graph")
        plt.axis('off')
        plt.show()

    def return_uncolored_graph(self):
        new_graph = self.graph.copy()
        colored_nodes = [idx for idx in self.colors.keys()]
        new_graph.remove_nodes_from(colored_nodes)
        return new_graph