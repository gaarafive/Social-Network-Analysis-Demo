# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:21:21 2020

"""
import networkx as nx
import matplotlib.pyplot as plt

g_fb = nx.read_edgelist('facebook_combined.txt', create_using = nx.Graph(), nodetype = int)

print(nx.info(g_fb))

# the graph is not directed
print (nx.is_directed(g_fb))


plt.axis('off')
spring_pos = nx.spring_layout(g_fb)
nx.draw_networkx(g_fb, pos = spring_pos, with_labels = False, node_size = 35)

# Degree Centrality
dg_centrality = nx.degree_centrality(g_fb)