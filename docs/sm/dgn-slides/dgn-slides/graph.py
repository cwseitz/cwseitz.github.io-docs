import matplotlib.pyplot as plt
import networkx as nx
from networkx import grid_graph

fig, ax = plt.subplots(1,2, figsize=(6,3))
G = nx.grid_2d_graph(25,25)

pos = {(x,y):(y,-x) for x,y in G.nodes()}
nx.draw(G, pos=pos, ax=ax[0],
        node_color='red',
        with_labels=False,
        node_size=5)

G = nx.random_geometric_graph(200, 0.125)
# position is stored as node attribute data for random_geometric_graph
pos = nx.get_node_attributes(G, 'pos')

# find node near center (0.5,0.5)
dmin = 1
ncenter = 0
for n in pos:
    x, y = pos[n]
    d = (x - 0.5)**2 + (y - 0.5)**2
    if d < dmin:
        ncenter = n
        dmin = d

# color by path length from node near center
p = dict(nx.single_source_shortest_path_length(G, ncenter))


nx.draw_networkx_edges(G, pos, ax=ax[1], nodelist=[ncenter], alpha=0.4)
nx.draw_networkx_nodes(G, pos, ax=ax[1], nodelist=list(p.keys()),
                       node_size=10,
                       node_color='red',
                       cmap=plt.cm.Reds_r)

ax[1].axis('off')
plt.tight_layout()
plt.show()
