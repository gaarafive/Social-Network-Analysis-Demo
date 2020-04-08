# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:35:38 2020

"""

import networkx as nx
import pandas as pd

G = nx.Graph()
# add node/edge pairs
G.add_node(0 ,location = (-106, 31), population = 674433)
G.add_node(1 ,location = (-118, 33), population = 448479)
G.add_node(2 ,location = (-96, 32), population = 84339)
G.add_node(3 ,location = (-122, 37), population = 1409019)
G.add_node(4 ,location = (-121, 38), population = 599164)
G.add_node(5 ,location = (-97, 37), population = 652405)
G.add_node(6 ,location = (-110, 32), population = 837442)
G.add_node(7 ,location = (-119, 36), population = 467007)
G.add_node(8 ,location = (-98, 29), population = 645966)
G.add_node(9 ,location = (-80, 35), population = 792862)
G.add_edge(0, 1, weight= 198)
G.add_edge(0, 2, weight= 336)
G.add_edge(0, 3, weight= 367)
G.add_edge(0, 5, weight= 322)
G.add_edge(1, 3, weight= 289)
G.add_edge(1, 6, weight= 333)
G.add_edge(3, 4, weight= 398)
G.add_edge(4, 5, weight= 290)
G.add_edge(4, 7, weight= 150)
G.add_edge(5, 8, weight= 295)
G.add_edge(8, 9, weight= 354)
nx.draw_networkx(G)

G.nodes(data=True)
df = pd.DataFrame(index=G.nodes())
df['location'] = pd.Series(nx.get_node_attributes(G, 'location'))
df['population'] = pd.Series(nx.get_node_attributes(G, 'population'))
df.head()
df['clustering'] = pd.Series(nx.clustering(G))
df['degree'] = pd.Series(G.degree())

G.edges(data=True)
df2 = pd.DataFrame(index=G.edges())
df2['weight'] = pd.Series(nx.get_edge_attributes(G, 'weight'))
df2['preferential attachment'] = [i[2] for i in nx.preferential_attachment(G, df2.index)]
df2['Common Neighbors'] = df2.index.map(lambda city: len(list(nx.common_neighbors(G, city[0], city[1]))))

