# cac ham truc quan hoa cua networkx

import networkx as nx
import matplotlib.pyplot as plt

# Instantiate the graph
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

# See what layouts are available in networkX
lstlayout = [x for x in nx.__dir__() if x.endswith('_layout')]
print(lstlayout)

# Drandom
plt.figure(figsize=(10,9))
pos = nx.fruchterman_reingold_layout(G)
#nx.draw_networkx(G, pos)

# ve theo bo cuc tron
plt.figure(figsize=(10,9))
pos = nx.circular_layout(G)
#nx.draw_networkx(G, pos)

# ve theo vi tri tuy chinh
plt.figure(figsize=(10,7))
pos = nx.get_node_attributes(G, 'location')
#nx.draw_networkx(G, pos)


# Draw graph with varying node color, node size, and edge width
plt.figure(figsize=(10,7))

node_color = [G.degree(v) for v in G]
#print(nx.get_node_attributes(G, 'population'))

node_size = [0.0005*nx.get_node_attributes(G, 'population')[v] for v in G]
edge_width = [0.0015*G[u][v]['weight'] for u,v in G.edges()]
#print(edge_width)
#nx.draw_networkx(G, pos, node_size=node_size, 
#                 node_color=node_color, alpha=0.7, with_labels=False, 
#                 width=edge_width, edge_color='.4', cmap=plt.cm.Blues)

plt.axis('off')
plt.tight_layout();


# Draw specific edges and add labels to specific nodes
plt.figure(figsize=(10,7))

node_color = [G.degree(v) for v in G]
node_size = [0.0005*nx.get_node_attributes(G, 'population')[v] for v in G]
edge_width = [0.0015*G[u][v]['weight'] for u,v in G.edges()]

nx.draw_networkx(G, pos, node_size=node_size, 
                 node_color=node_color, alpha=0.7, with_labels=False, 
                 width=edge_width, edge_color='.4', cmap=plt.cm.Blues)


greater_than_770 = [x for x in G.edges(data=True) if x[2]['weight']>770]
#nx.draw_networkx_edges(G, pos, edgelist=greater_than_770, edge_color='r', alpha=0.4, width=6)

#nx.draw_networkx_labels(G, pos, labels={0: 'lb1', 5: 'lb2'}, font_size=18, font_color='w')

plt.axis('off')
plt.tight_layout();
