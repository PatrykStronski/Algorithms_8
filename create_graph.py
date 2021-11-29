import networkx as nx
import random

capacity_interval = (1, 20)
nodes = [x for x in range(0, 14)]
edges_all = [
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 7),
    (7, 9),
    (9, 13),
    (2, 7),
    (7, 8),
    (8, 10),
    (10, 13),
    (3, 4),
    (4, 2),
    (4, 6),
    (6, 1),
    (6, 12),
    (6, 11),
    (12, 13),
    (11, 13),
    (3, 5),
    (5, 6)
]

def generate_rand_different(strt: int, end: int, without: int) -> int:
    v2 = random.randint(strt, end)
    while v2 == without:
        v2 = random.randint(strt, end)
    return v2


def create_random_graph(node_number: int) -> nx.DiGraph:
    graph = nx.complete_graph(node_number, nx.DiGraph(capacity=1))
    for e in graph.nodes():
        capacity = random.randint(capacity_interval[0], capacity_interval[1])
        graph.add_edge(e[0], e[1], capacity=capacity)
    return graph

def create_random_flow_graph(node_number: int, max_connections = 3) -> nx.DiGraph:
    edges = []
    g = nx.DiGraph(edges)

    for v1 in range(0, node_number):
        for cons in range(0, max_connections):
            if random.random() < 0.2:
                continue
            v2 = generate_rand_different(1, node_number, v1)
            while (v2, v1) in edges or (v1, v2) in edges:
                v2 = generate_rand_different(1, node_number, v1)
            g.add_edge(v1, v2, capacity=random.randint(1, 20))
    return g

        

def create_hardcoded_graph() -> nx.DiGraph:
    g = nx.DiGraph()
    for e in edges_all:
        capacity = random.randint(capacity_interval[0], capacity_interval[1])
        g.add_edge(e[0], e[1], capacity=capacity)
    return g

