# pygraphs

A package for the study of graph discrete data structures and algorithms.


## Usage

### Installation

At this point, distributed packages are compatible with Linux only.

1. Install via [pip](https://test.pypi.org/project/pygraphs/):

    ```python3 -m pip install --user --index-url https://test.pypi.org/simple/ --no-deps pygraphs```

2. Import the package:

    ```import pygraphs as pyg```

### Features

- Efficient data structures written in modern C++ are available.
  - Directed and Undirected Graph templates.
  - Priority Queues using Heaps.
  - Disjoint Sets.
- Classic algorithms are implemented in Python with type annotations.
  - Breadth-First and Depth-First Searches.
  - Eulerian cycle in Hierholzer's algorithm.
  - Hamiltonian cycle (TSP) using Bellman-Held-Karp.
  - Shortest Path with Bellman-Ford, Dijkstra and Floyd-Warshall algorithms.


## Build process

Source code is made available in [our git repo](https://gitlab.com/baioc/pygraphs).

Data structures and some key operations are implemented in C++17 (compiled using GCC 9.1.0) and wrapped into Python 3.6+ with [Swig](http://www.swig.org/) (version 4.0.0).
