# Copyright (c) 2019 Gabriel B. Sant'Anna <baiocchi.gabriel@gmail.com>
# @License Apache <https://gitlab.com/baioc/pygraphs>

from libpygraphs import Graph, Digraph
from common import Node, graph_edges
from math import inf
from typing import Dict, Tuple, Set, Generator, Sequence
from collections import deque


def max_flow(graph: Digraph, source: Node, sink: Node) \
        -> Dict[Tuple[Node, Node], float]:
    """Find the maximum flow through a digraph by Edmonds-Karp FFA. O(V * E^3)
    Returns a dictionary maping edges to their maximum flow in the network."""

    flow = {pipe: 0 for pipe in graph_edges(graph)}

    def residue(u: Node, v: Node) -> float:
        return graph.weight(u, v) - flow[(u, v)]

    while True:
        pred: Dict[Node, Node] = {}

        queue = deque()
        queue.append(source)
        while len(queue) > 0:
            u = queue.popleft()
            for v in graph.neighbours(u):
                if v not in pred and v != source and residue(u, v) > 0:
                    pred[v] = u
                    queue.append(v)

        if sink not in pred:
            break

        capacity = inf
        v = sink
        while v in pred:
            u = pred[v]
            capacity = min(capacity, residue(u, v))
            v = u

        for uv in flow.keys():
            flow[uv] += capacity

    return flow


def _test_flow():
    V: Set[Node] = {'S', 'A', 'B', 'C', 'D', 'T'}
    E: Set[Tuple[Node, Node]] = {('S', 'A', 5), ('S', 'B', 5),
                                 ('A', 'B', 10), ('A', 'C', 5), ('C', 'T', 5),
                                 ('B', 'D', 5), ('D', 'T', 5)}

    G: Digraph = Digraph(len(V))
    for (u, v, w) in E:
        G.link(u, v, w)

    F = max_flow(G, 'S', 'T')
    for (u, v), flow in F.items():
        print(u, v, flow)
