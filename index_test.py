from create_graph import create_random_flow_graph
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.flow import preflow_push, edmonds_karp
import math
import statistics
import time

nmbs = range(10, 1000)
REPEATS = 5

g = create_random_flow_graph(20, 5)
nx.draw(g)
plt.show()

rek = edmonds_karp(g, 0, 19)
print(rek.graph['flow_value'])
rpp = preflow_push(g, 0, 19)
print(rek.graph['flow_value'])
