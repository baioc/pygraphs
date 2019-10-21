# pygraphs on wheels

A package for the study of graph discrete data structures and algorithms.


## Usage

### Installation

At this point, distributed packages are compatible with Linux only.

1. Install via [pip](https://test.pypi.org/project/pygraphs/):</br>
    ```pip install --user -i https://test.pypi.org/simple/ pygraphs```

2. Import the package:</br>
    ```import pygraphs as pyg```

### Features

- Efficient data structures written in modern C++ are available.
  - Directed and undirected Graphs.
  - Priority Queue using binary heap.
  - Disjoint Sets as linked lists.
- Classic algorithms are implemented in Python with type annotations.
  - Breadth-First and Depth-First Searches.
  - Eulerian cycle in Hierholzer's algorithm.
  - Hamiltonian cycle (TSP) using Bellman-Held-Karp.
  - Shortest path with Bellman-Ford, Dijkstra and Floyd-Warshall algorithms.
  - Minimum spanning trees through Prim.


## Build process

Source code is made available in [our git repo](https://gitlab.com/baioc/pygraphs).

Data structures and some key operations are implemented in C++17 (compiled with gcc 9.1.0) and wrapped into Python 3.6+ with [Swig](http://www.swig.org/) (version 4.0.0).
