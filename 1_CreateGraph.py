import networkx as nx
# create graph
G = nx.Graph()

# create node and edge
G.add_edges_from([(0, 1),
                   (0, 2),
                   (1, 3),
                   (1, 6),
                   (3, 4),])


# draw
nx.draw_networkx(G)


# degree
vdegree = nx.degree(G, 0)
#print(vdegree)


# shortest path
vsortestpath = nx.shortest_path(G, 0)
#print(vsortestpath)
vsortestpathlength = nx.shortest_path_length(G, 0)
#print(vsortestpathlength)
#print(nx.average_shortest_path_length(G))

# eccentricity
print(nx.eccentricity(G))
print(nx.radius(G))
print(nx.periphery(G))
# list of all adges
#print('list of all adges: ')
#print(G.edges())


# list of all adge with atributes
#print('list of all adges with atributes: ')
#print(G.edges(data = True))


# breadth-First Search
GT = nx.bfs_tree(G,0)
#nx.draw_networkx(GT)

