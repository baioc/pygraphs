from .libpygraphs import Graph, Digraph, PrioQ

from math import inf
from typing import NewType as _NewType

Label = _NewType('Label', str)
Weight = _NewType('Weight', float)

from .common import graph_edges, arbitrary
from .search import breadth_first, depth_first
from .cycle import eulerian_cycle, hamiltonian_circuit
from .path import shortest_routes, shortest_paths, shortest_network
from .forest import min_tree, toposort, components
