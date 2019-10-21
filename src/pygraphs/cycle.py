# Copyright (c) 2019 Gabriel B. Sant'Anna <baiocchi.gabriel@gmail.com>
# @License Apache <https://gitlab.com/baioc/pygraphs>

from .libpygraphs import Digraph, Graph
from .common import Node, graph_edges, arbitrary, T
from typing import Set, Tuple, List, Optional, Sequence, TypeVar, Generator, \
                   Union, Dict, FrozenSet
from math import inf
from itertools import combinations


def eulerian_cycle(graph: Union[Graph, Digraph],
                   initial: Optional[Node] = None) -> List[Node]:
    """Finds an eulerian cycle on a graph using Hierholzer's algorithm.

    Returns a list representing the node path order of the eulerian cycle, it
    is empty when no such cycle is found.
    """

    def Hierholzer(graph: Union[Graph, Digraph],
                   initial: Node,
                   traversed: Set[Tuple[Node, Node]]) -> List[Node]:
        def splicycle(cycle: List[T], subcycle: List[T]) -> List[T]:
            pos = cycle.index(subcycle[0])
            return cycle[:pos] + subcycle + cycle[pos+1:]

        cycle = [initial]
        u = initial
        while True:
            e = None
            for v in graph.neighbours(u):
                if (u, v) not in traversed:
                    e = (u, v)
                    break
            else:  # no break: every edge (u,v) has already been traversed
                return []

            (u, v) = e
            traversed.add(e)
            if not graph.directed():
                traversed.add((v, u))
            cycle.append(v)
            u = v
            if u == initial:
                break

        for v in cycle:
            for w in graph.neighbours(v):
                if (v, w) not in traversed:
                    subcycle = Hierholzer(graph, v, traversed)
                    if len(subcycle) == 0:
                        return []
                    else:
                        cycle = splicycle(cycle, subcycle)

        return cycle

    traversed: Set[Tuple[Node, Node]] = set()
    initial = arbitrary(graph.nodes()) if initial is None else initial
    cycle = Hierholzer(graph, initial, traversed)
    if len(cycle) == 0:
        return []
    else:
        for (u, v) in graph_edges(graph):
            if (u, v) not in traversed:
                return []
        else:  # no break
            return cycle


def hamiltonian_circuit(graph: Union[Graph, Digraph], begin: Node) \
        -> Tuple[float, List[Node]]:
    """Finds a graph's minimal hamiltonian circuit through Bellman-Held-Karp.

    Supposes the graph is connected and has at least one hamiltonian cycle.

    Returns a tuple containing the total cost of the optimal circuit path
    and the path itself as a list (infinity and [] when none is found).
    """

    # Visits, FinalDestination, Cost = FrozenSet[Node], Node, float
    cost: Dict[Tuple[FrozenSet[Node], Node], float] = {}
    dests = frozenset({v for v in graph.nodes() if v != begin})

    for place in dests:
        cost[(frozenset({place}), place)] = graph.weight(begin, place)

    for size in range(2, graph.node_number()):
        for itinerary in combinations(dests, size):
            route = frozenset(itinerary)
            for final in route:
                sub = route - {final}
                opt = inf  # optimal solution for problem subset
                for mid in sub:
                    opt = min(opt, cost[(sub, mid)] + graph.weight(mid, final))
                cost[(route, final)] = opt

    minimum = inf
    for end in dests:
        minimum = min(minimum, cost[(dests, end)] + graph.weight(end, begin))

    # check if no circuit was found
    if minimum == inf:
        return (inf, [])

    # backtrack to find full path
    circuit = minimum
    path: List[Node] = [begin]

    for _ in range(graph.node_number() - 1):
        for (route, final), opt in cost.items():
            if (circuit - graph.weight(final, path[-1]) == opt):
                path.append(final)
                circuit = opt
                break

    path.append(begin)
    path.reverse()

    return (minimum, path)


def _test_cycle():
    V: Set[Node] = {'a', 'b', 'c', 'd', 'e'}
    E: Set[Tuple[Node, Node, float]] = {('b', 'a', 2.5), ('a', 'c', 3),
                                        ('c', 'd', 2.5), ('d', 'b', 1),
                                        ('a', 'e', 4), ('e', 'c', 2),
                                        ('e', 'b', 1.5), ('d', 'e', 2)}
    G: Union[Graph, Digraph] = Graph(len(V))
    for (u, v, w) in E:
        G.link(u, v, w)

    C = hamiltonian_circuit(G, 'a')
    print(C)