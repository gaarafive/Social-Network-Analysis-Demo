import networkx as nx

G = nx.DiGraph()
G.add_edges_from([('A', 'B'), ('C', 'A'), ('A', 'E'), ('G', 'A'), 
                  ('A', 'N'), ('B', 'C'), ('D', 'B'), ('B', 'E'), 
                  ('C', 'D'), ('E', 'C'), ('D', 'E'), ('E', 'D'), 
                  ('F', 'G'), ('I', 'F'), ('J', 'F'), ('H', 'G'), 
                  ('I', 'G'), ('G', 'J'), ('I', 'H'), ('H', 'I'), 
                  ('I', 'J'), ('J', 'O'), ('O', 'J'), ('K', 'M'), 
                  ('K', 'L'), ('O', 'K'),('O', 'L'), ('N', 'L'), 
                  ('L', 'M'), ('N', 'O')])

nx.draw_networkx(G)

# connected graph
nx.is_weakly_connected(G)
nx.is_strongly_connected(G)



# disconnect graph
nx.node_connectivity(G,'G','E')
print(nx.minimum_node_cut(G,'G','E'))

nx.edge_connectivity(G, 'G','L')
print(nx.minimum_node_cut(G,'G','L'))

