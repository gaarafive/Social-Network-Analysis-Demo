# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:14:45 2020

@author: Admin
"""

import networkx as nx
import matplotlib.pyplot as plt

# Degree distribution

G = nx.Graph()
G.add_edges_from([('A', 'B'),
                   ('B', 'C'),
                   ('C', 'E'),
                   ('C', 'D'),
                   ('F', 'G'),
                   ('A', 'G'),
                   ('A', 'H'),
                   ('G', 'H'),
                   ('G', 'I'),
                   ('F', 'I'),
                   ('D', 'F')])
#nx.draw_networkx(G)

degrees = G.degree()
degrees_values = [v for k, v in degrees]

histogram = [list(degrees_values).count(i)/float(nx.number_of_nodes(G)) for i in degrees_values]

plt.bar(degrees_values, histogram)
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.show()

# In-Degree distribution

G = nx.DiGraph()
G.add_edges_from([('A', 'B'),
                   ('B', 'C'),
                   ('C', 'E'),
                   ('C', 'D'),
                   ('F', 'G'),
                   ('A', 'G'),
                   ('A', 'H'),
                   ('G', 'H'),
                   ('G', 'I'),
                   ('F', 'I'),
                   ('D', 'F')])
#nx.draw_networkx(G)

degrees = G.in_degree()
degrees_values = [v for k, v in degrees]

histogram = [list(degrees_values).count(i)/float(nx.number_of_nodes(G)) for i in degrees_values]

plt.bar(degrees_values, histogram)
plt.xlabel('In Degree')
plt.ylabel('Fraction of Nodes')
plt.show()


# Preferential Attachment
B = nx.barabasi_albert_graph(1000,1)

degrees = B.degree()
degrees_values = [v for k, v in degrees]

histogram = [list(degrees_values).count(i)/float(nx.number_of_nodes(B)) for i in degrees_values]

plt.plot(degrees_values, histogram,'o')
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.xscale('log')
plt.yscale('log')
plt.show()

# Small World Model
import networkx as nx
import matplotlib.pyplot as plt

B = nx.watts_strogatz_graph(1000,6, 0.04)
degrees = B.degree()
degrees_values = [v for k, v in degrees]
histogram = [list(degrees_values).count(i)/float(nx.number_of_nodes(B)) for i in degrees_values]
plt.plot(degrees_values, histogram,'o')
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.show()


