import networkx as nx
import matplotlib.pyplot as plt


class GraphVisualization(object):
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def Visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()


G = GraphVisualization()
G.addEdge('k1', 'k2')
G.addEdge('k1', 'k3')
G.addEdge('k1', 'k4')
G.addEdge('k1', 'k5')
G.addEdge('k1', 'k6')
G.addEdge('k2', 'k1')
G.addEdge('k2', 'k3')
G.addEdge('k2', 'k4')
G.addEdge('k2', 'k5')
G.addEdge('k2', 'k6')
G.addEdge('k3', 'k1')
G.addEdge('k3', 'k2')
G.addEdge('k3', 'k4')
G.addEdge('k3', 'k5')
G.addEdge('k3', 'k6')
G.addEdge('k4', 'k1')
G.addEdge('k4', 'k2')
G.addEdge('k4', 'k3')
G.addEdge('k4', 'k6')
G.addEdge('k5', 'k1')
G.addEdge('k5', 'k2')
G.addEdge('k5', 'k3')
G.addEdge('k5', 'k6')
G.addEdge('k6', 'k1')
G.addEdge('k6', 'k2')
G.addEdge('k6', 'k3')
G.addEdge('k6', 'k4')
G.addEdge('k6', 'k5')
G.Visualize()