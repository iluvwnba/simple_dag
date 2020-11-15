from __future__ import annotations

import uuid
from collections import deque, defaultdict
from typing import List, Dict, Iterator, DefaultDict, Deque


class DAGError(Exception):
    pass


'''
Known
Each point is called a vertex - noted using v or _v
'''


class Vertex:
    def __init__(self, v_id: str = None):
        if v_id:
            self.id = v_id
        else:
            # Validate is unique
            self.id: str = str(uuid.uuid4())[:4]

    def __repr__(self):
        return self.id


'''
From airflow docs
chain(t1, [t2, t3], [t4, t5], t6)

    is equivalent to::

         / -> t2 -> t4 \
       t1               -> t6
         \ -> t3 -> t5 /

t1.set_downstream(t2)
t1.set_downstream(t3)
t2.set_downstream(t4)
t3.set_downstream(t5)
t4.set_downstream(t6)
t5.set_downstream(t6)
'''


class GraphBase:
    '''
    Graph is always empty to start with
    '''

    def __init__(self):
        self._in_degree: Dict[int, int]() = dict()
        self._V: int = 0
        self._E: int = 0
        self._adj: DefaultDict[(Vertex, List[Vertex])] = defaultdict(list)

    def no_of_edges(self) -> int:
        return self._E

    def no_of_vertices(self) -> int:
        return self._V

    def in_degree(self, v: Vertex):
        self.validate_vertex(v)
        return self._in_degree[v]

    def out_degree(self, v: Vertex):
        self.validate_vertex(v)
        return len(self._adj[v])

    def validate_vertex(self, v: Vertex) -> bool:
        return True

    '''
    @param v the vertex
    @return the adjacent vertex
    '''

    def adj(self, v: Vertex) -> Iterator[Vertex]:
        if not self.validate_vertex(v):
            raise Exception()
        return self._adj[v]

    def add_edge(self, v: Vertex, w: Vertex):
        if self.validate_vertex(v) and self.validate_vertex(w):
            self._adj[v].append(w)
            if w in self._in_degree:
                self._in_degree[w] = self._in_degree[w] + 1
            else:
                self._in_degree[w] = 1
            self._E += 1
        else:
            raise Exception()

    def print_tree(self) -> None:
        def print_downstream(v: Vertex, level=0):
            print((" " * level * 4) + str(v))
            level += 1
            for v_1 in self.adj(v):
                print_downstream(v_1, level=level)

        # Get first element of the graph
        print_downstream(list(self._adj)[0])

    def __len__(self):
        return self.no_of_edges()


class DAG(GraphBase):

    def __init__(self):
        super().__init__()
        # has vertex v been _visited
        self._visited: Dict[(str, bool)] = dict()
        # is vertex on the stack
        self._explore: Dict[(str, bool)] = dict()
        self._topological_order: Deque[Vertex] = deque()

    def _has_cycle(self) -> bool:
        return not len(self._topological_order)

    def check_cycle(self) -> bool:
        V: List[Vertex] = list(self._adj)
        for v in V:
            if v not in self._visited:
                if self._dfs(v):
                    return True
        return False

    '''
    Not useful
    https://algs4.cs.princeton.edu/42digraph/DirectedCycle.java.html
    https://algs4.cs.princeton.edu/42digraph/Topological.java.html
    '''

    def _dfs(self, v: Vertex) -> bool:
        if v in self._visited:
            if self._visited[v]:
                return False
        # Have already been to the vertex, there is a cycle
        if v in self._explore:
            if self._explore[v]:
                return True

        self._explore[v] = True

        for w in self.adj(v):
            if w not in self._visited:
                if self._dfs(w):
                    return True

        self._explore[v] = False
        self._visited[v] = True
        self._topological_order.appendleft(v)
        return False

    def topological_order(self) -> Iterator[Vertex]:
        if self._topological_order:
            return self._topological_order
        return list()

    '''
    Expected File Format(txt)
    number of vectors
    number of edges
    v_edge w_edge
    v_edge w_edge
    v_edge w_edge
    '''

    @staticmethod
    def load_DAG_from_file(file: str) -> DAG:
        with open(file, 'rt') as f:
            # Double header
            d = DAG()
            d._E = int(next(f))
            d._V = int(next(f))
            for line in f:
                v = line.split(' ')
                d.add_edge(Vertex(v_id=v[0]), Vertex(v_id=v[1]))
        return d
