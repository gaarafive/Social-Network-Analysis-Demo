import networkx as nx

# create graph 

G = nx.DiGraph()
G.add_edges_from([(0, 1),
                   (0, 2),
                   (1, 3),
                   (1, 6),
                   (3, 4),])

#nx.draw_networkx(G)

# 1.	Degree centrality
nx.degree_centrality(G)

# 2.	Closeness centrality
nx.closeness_centrality(G)
nx.shortest_path_length(G, 0)

# 3.	betweenness centrality
nx.betweenness_centrality(G)
nx.betweenness_centrality(G, normalized = True, k = 5)
nx.edge_betweenness_centrality(G)

#4 Page Rank
pr = nx.pagerank(G, alpha=0.9, max_iter=50)

#5 HITS
pr = nx.hits(G)




