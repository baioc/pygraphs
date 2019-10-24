# Copyright (c) 2019 Gabriel B. Sant'Anna <baiocchi.gabriel@gmail.com>
# @License Apache <https://gitlab.com/baioc/pygraphs>

from .libpygraphs import Graph, PrioQ, Digraph
from .common import Node, arbitrary
from typing import Set, Tuple, Dict, Optional, Sequence, List, Iterable
from math import inf
from collections import deque


def minimum_spanning_forest(graph: Graph, start: Node = None) \
        -> Dict[Node, Optional[Node]]:
    """
    Find the minimum spanning forest of an undirected graph via Prim.

    Returns a dictionary containing nodes as keys that map to their parent
    node in the tree they're in.
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


def toposort(graph: Digraph) -> Sequence[Node]:
    """Topologically sort a directed graph's vertices using Tarjan's DFS.
    Returns a sequence containing the result of the partial ordering."""

    def dfs_ord(graph: Digraph, root: Node, visited: Set[Node], order):
        if root in visited:
            return

        visited.add(root)
        for v in graph.neighbours(root):
            dfs_ord(graph, v, visited, order)

        order.insert(0, root)

    visited: Set[Node] = set()
    order = deque()
    for u in graph.nodes():
        dfs_ord(graph, u, visited, order)

    return order


def connected_components(graph: Digraph) -> Iterable[Set[Node]]:
    """
    Find a digraph's strongly connected components using Kosaraju's algorithm.

    Returns an iterable containing each component of the graph's partitioning.
    """

    def dfs_visit(graph: Digraph,
                  root: Node,
                  visited: Set[Node],
                  stack: List[Node],
                  connections: Dict[Node, Set[Node]]):
        if root not in visited:
            visited.add(root)

            for child in graph.neighbours(root):
                connections[child].add(root)
                dfs_visit(graph, child, visited, stack, connections)

            stack.append(root)

    def component_assign(child: Node,
                         root: Node,
                         components: Dict[Node, Set[Node]],
                         connections: Dict[Node, Set[Node]]):
        if child in connections.keys():
            if root not in components:
                components[root] = set()

            components[root].add(child)

            neighbours = connections[child]
            connections.pop(child)

            for neighbour in neighbours:
                component_assign(neighbour, root, components, connections)

    visited: Set[Node] = set()
    stack: List[Node] = []
    connections: Dict[Node, Set[Node]] = {v: set() for v in graph.nodes()}

    for u in graph.nodes():
        if u not in visited:
            dfs_visit(graph, u, visited, stack, connections)

    components: Dict[Node, Set[Node]] = {}

    while len(stack) > 0:
        u = stack.pop()
        component_assign(u, u, components, connections)

    return components.values()


def _test_forest():
    V: Set[Node] = {'a', 'b', 'c', 'd', 'e'}
    E: Set[Tuple[Node, Node, float]] = {('a', 'b', 3), ('c', 'a', 2),
                                        ('c', 'd', 1), ('c', 'e', 3),
                                        ('d', 'e', 2), ('b', 'd', 4)}
    G: Graph = Graph(len(V))
    for (u, v, w) in E:
        G.link(u, v, w)

    A = minimum_spanning_forest(G, 'a')
    print(A)


def _test_sort():
    V: Set[Node] = {'5', '7', '3', '11', '8', '2', '9', '10'}
    E: Set[Tuple[Node, Node]] = {('5','11'), ('7','11'), ('7','8'), ('3','8'),
                                 ('3','10'), ('11','2'), ('11','9'), ('8','9'),
                                 ('11','10')}
    G: Digraph = Digraph(len(V))
    for (u, v) in E:
        G.link(u, v)

    tord = toposort(G)
    print(tord)


def _test_connect():
    V: Set[Node] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    E: Set[Tuple[Node, Node]] = {('a','b'), ('b','e'), ('e','a'),
                                 ('f','g'), ('g','f'),
                                 ('c','d'), ('d','c'), ('d','h'), ('h','d'),
                                 ('b','c'),
                                 ('b','f'), ('e','f'),
                                 ('c','g'), ('h','g')}
    G: Digraph = Digraph(len(V))
    for (u, v) in E:
        G.link(u, v)

    print(connected_components(G))
