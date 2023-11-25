import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np

num_agents = 99

# Create two separate networks
group1 = nx.complete_graph(int(num_agents / 2))
group2 = nx.complete_graph(math.ceil(num_agents / 2))

# Renaming nodes in group2 to have distinct node names
group2 = nx.relabel_nodes(group2, {node: node + int(num_agents / 2) for node in group2.nodes})

print('group1: ', nx.nodes(group1))
print('group2: ', nx.nodes(group2))

# Connect the networks by a few edges
cross_edges = []
for _ in range(int(num_agents * .05)):
    cross_edges.append((np.random.randint(0, int(num_agents / 2)),
                        np.random.randint(int(num_agents / 2), num_agents)))
print(cross_edges)
exit()