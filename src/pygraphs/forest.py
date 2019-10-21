# Copyright (c) 2019 Gabriel B. Sant'Anna <baiocchi.gabriel@gmail.com>
# @License Apache <https://gitlab.com/baioc/pygraphs>

from .libpygraphs import Digraph, Graph, PrioQ
from .common import Node, arbitrary
from typing import Set, Tuple, Union, Dict, Optional
from math import inf


def minimum_spanning_forest(graph: Union[Graph, Digraph], start: Node = None) \
        -> Dict[Node, Optional[Node]]:
    """
    Find the minimum spanning forest of a graph using Prim's algorithm.

    Returns a dictionary containing nodes as keys that map to their parent
    node in their search tree.
    """

    start = arbitrary(graph.nodes()) if start is None else start
    ancestors: Dict[Node, Optional[Node]] = {}
    queue = PrioQ()
    for v in graph.nodes():
        ancestors[v] = None
        queue.enqueue(v, inf if v != start else 0)

    while not queue.empty():
        u = queue.dequeue()
        for v in graph.neighbours(u):
            if queue.contains(v) and graph.weight(u, v) < queue.priority(v):
                ancestors[v] = u
                queue.update(v, graph.weight(u, v))

    return ancestors


def _test_forest():
    V: Set[Node] = {'a', 'b', 'c', 'd', 'e'}
    E: Set[Tuple[Node, Node, float]] = {('a', 'b', 3), ('c', 'a', 2),
                                        ('c', 'd', 1), ('c', 'e', 3),
                                        ('d', 'e', 2), ('b', 'd', 4)}
    G: Union[Graph, Digraph] = Digraph(len(V))
    for (u, v, w) in E:
        G.link(u, v, w)

    A = minimum_spanning_forest(G)
    print(A)
