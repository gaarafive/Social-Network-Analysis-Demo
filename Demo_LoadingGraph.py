# Những cách khác nhau mà biểu đồ mạng có thể được trình bày hay load các định dạng khác nhau bằng networkx

import networkx as nx
import numpy as np
import pandas as pd
import matplotlib

# Instantiate the graph
G1 = nx.Graph()
# add node/edge pairs
G1.add_edges_from([(0, 1),
                   (0, 2),
                   (0, 3),
                   (0, 5),
                   (1, 3),
                   (1, 6),
                   (3, 4),
                   (4, 5),
                   (4, 7),
                   (5, 8),
                   (8, 9)])

# draw the network G1
nx.draw_networkx(G1)


# Adjacency List
# G_adjlist.txt

# 0 1 2 3 5
# 1 3 6
# 2
# 3 4
# 4 5 7
# 5 8
# 6
# 7
# 8 9
# 9

G2 = nx.read_adjlist('G_adjlist.txt', nodetype=int)
print(G2.edges())

# Adjacency Matrix
# Các phần tử trong ma trận kề cho biết các cặp đỉnh có liền kề hay không trong biểu đồ. 
# Mỗi nút có một hàng và cột tương ứng. Ví dụ, hàng 0, cột 1 tương ứng với cạnh giữa nút 0 và nút 1.

G_mat = np.array([[0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                  [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
print(G_mat)
G3 = nx.Graph(G_mat)
print(G3.edges())

# Edgelist
# Định dạng danh sách cạnh thể hiện các cặp cạnh trong hai cột đầu tiên.
# Các thuộc tính cạnh bổ sung có thể được thêm vào trong các cột tiếp theo.
G4 = nx.read_edgelist('G_edgelist.txt', data=[('Weight', int)])
print(G4.edges(data=True))




#Pandas DataFrame
#Đồ thị cũng có thể được tạo từ các tệp dữ liệu Pandas DataFrame nếu chúng ở định dạng danh sách cạnh
G_df = pd.read_csv('G_edgelist.txt', delim_whitespace=True, 
                   header=None, names=['n1', 'n2', 'weight'])
print(G_df)

G5 = nx.from_pandas_edgelist(G_df, 'n1', 'n2', edge_attr='weight')
G5.edges(data=True)





































