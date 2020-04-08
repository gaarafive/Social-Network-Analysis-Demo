
import networkx as nx
# create graph
G = nx.Graph()
G.add_edges_from([('A', 'B'),
                  ('B','C'),
                  ('A', 'D'),
                  ( 'B', 'D'), 
                  ('D', 'C'), 
                  ('A', 'E'), 
                  ('C', 'F'), 
                  ('A', 'E'), 
                  ('E', 'G'), 
                  ('F', 'G'),
                  ('E' , 'F'), 
                  ('G', 'H'), 
                  ('G', 'I')])

nx.draw_networkx(G)

# Common neighbors 
Comm_neigh = [(e[0], e[1], len(list(nx.common_neighbors(G, e[0], e[1])))) for e in nx.non_edges(G)]


# Jaccard Coefficient
jacc_coefficient = list(nx.jaccard_coefficient(G))

# Resource Allocation Index
resource_allocation_index = list(nx.resource_allocation_index(G))
# Adamic Adar Index
adamic_adar_index = list(nx.adamic_adar_index(G))

pref_attachment = list(nx.preferential_attachment(G))

# Community Structure
G2 =  nx.Graph()
G2.add_node('A', community = 0)
G2.add_node('B', community = 0)
G2.add_node('C', community = 0)
G2.add_node('D', community = 0)
G2.add_node('E', community = 1)
G2.add_node('F', community = 1)
G2.add_node('G', community = 1)
G2.add_node('H', community = 1)
G2.add_node('I', community = 1)
G2.add_edges_from([('A', 'B'),
                  ('B','C'),
                  ('A', 'D'),
                  ( 'B', 'D'), 
                  ('D', 'C'), 
                  ('A', 'E'), 
                  ('C', 'F'), 
                  ('A', 'E'), 
                  ('E', 'G'), 
                  ('F', 'G'),
                  ('E' , 'F'), 
                  ('G', 'H'), 
                  ('G', 'I')])

#nx.draw_networkx(G2)
# community communition neighbors
sh = list(nx.cn_soundarajan_hopcroft(G2))

# community Resource Allocation
ra = list(nx.ra_index_soundarajan_hopcroft(G2))