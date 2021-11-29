from create_graph import create_random_flow_graph
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.flow import preflow_push, edmonds_karp
import math
import time
import os, psutil
process = psutil.Process(os.getpid())

nmbs = range(10, 1000)
REPEATS = 5

g = create_random_flow_graph(20, 5)
nx.draw(g, with_labels = True)
plt.savefig('./example_flow_net.png')
plt.show()

times_ek = []
mem_ek = []
times_pp = []
mem_pp = []
edges_nmbs = []

max_flow_ek = []
max_flow_pp = []

for nmb in nmbs:
    g = create_random_flow_graph(nmb, 10 + int(math.log(nmb, 2)))
    t_ek = 0
    t_pp = 0
    m_ek = 0
    m_pp = 0
    f_ek = 0
    f_pp = 0
    for r in range(0, REPEATS):
        strt = time.time()
        rek = edmonds_karp(g, 0, nmb)
        end = time.time()
        m_ek += (process.memory_info().rss/1024/1024)/5 
        t_ek += (end - strt)/5
        f_ek += rek.graph['flow_value']/5

        strt = time.time()
        rpp = preflow_push(g, 0, nmb)
        end = time.time()
        m_pp += (process.memory_info().rss/1024/1024)/5 
        t_pp += (end - strt)/5 
        f_pp += rpp.graph['flow_value']/5
    edges_nmbs.append(len(g.edges()))
    e = len(g.edges())
    times_ek.append(t_ek)
    times_pp.append(t_pp)
    mem_ek.append(m_ek)
    mem_pp.append(m_pp)
    max_flow_ek.append(f_ek)
    max_flow_pp.append(f_pp)

single_time_ek = t_ek/(len(g.nodes()) * e ** 2)
single_time_pp = t_pp/(len(g.nodes()) ** 2 * math.sqrt(e))

#running time O(|V|*|E|^2)
plt.scatter(x=nmbs, y=times_ek, label='Edmonds Karp alg', marker='+', alpha=0.2)
plt.plot(nmbs, [nmb * edges_nmbs[n-10] ** 2 * single_time_ek for n in nmbs], label='Predicted result')
plt.legend()
plt.title('Execution time [s] for Edmonds-Karp algorithm')
plt.savefig('./edmonds_karp.png')
plt.show()

#running time O(|V|^2* SQRT(|E|))
plt.scatter(x=nmbs, y=times_pp, label='Preflow Push algorithm', marker='+', alpha=0.2)
plt.plot(nmbs, [nmb ** 2 * math.sqrt(edges_nmbs[n-10])  * single_time_pp for n in nmbs], label='Predicted result')
plt.legend()
plt.title('Execution time [s] for Preflow-Push algorithm')
plt.savefig('./preflow_push.png')
plt.show()

#MEM estimation
plt.scatter(x=nmbs, y=mem_ek, label='Edmonds Karp alg', marker='+', alpha=0.2)
plt.legend()
plt.title('Memory usage [MB] for Edmonds Karp algorithm')
plt.savefig('./edmonds_karp_mem.png')
plt.show()

plt.scatter(x=nmbs, y=mem_pp, label='Preflow Push algorithm', marker='+', alpha=0.2)
plt.legend()
plt.title('Memory usage [MB] for Preflow-Push algorithm')
plt.savefig('./preflow_push_mem.png')
plt.show()

#flow values

plt.plot(nmbs, max_flow_ek, label='Edmonds-Karp Algorithm', linewidth=5, alpha=0.5)
plt.plot(nmbs, max_flow_pp, label='Preflow-Push Algorithm')
plt.legend()
plt.savefig('./result_comparison.png')
plt.title('Results of the algorithms')
plt.show()
