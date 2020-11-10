from __future__ import annotations
from typing import List, Dict, Iterator, Counter


class DAGError(Exception):
    pass


'''
Known
Each point is called a vertex - noted using v or _v
Each 
Questions
Do you just store a dictionary of task_ids, vertexs
Is a DAG a namespace thats gets sorted at runtime to understand running order -
    Do vertexs just manage there own dependents
ACII tree view implementation
'''



class DAG:
    '''
    DAGS are always empty to start with
    V = Size
    TODO - Can size be dynamic
    '''

    def __init__(self, V: int):
        if V < 0:
            raise Exception()
        self._in_degree: Dict[int, int]() = {}
        self._V = V
        self._E: int = 0
        self._adj: Counter[int] = {}
        for v in range(self._V):
            self._adj[v]: List[int]() = list()

    def no_of_edges(self) -> int:
        return self._E

    def no_of_vertices(self) -> int:
        return self._V

    def in_degree(self, v: int):
        self.validate_vertex(v)
        return self._in_degree[v]

    def out_degree(self,v: int):
        self.validate_vertex(v)
        return len(self._adj[v])


    def validate_vertex(self, v: int) -> bool:
        if v < 0 or v >= self._V:
            return False
        return True

    '''
    @param v the vertex
    @return the adjacent vertex
    '''
    def adj(self, v: int) -> Iterator[int]:
        if not self.validate_vertex(v):
            raise Exception()
        return self._adj[v]


    def add_vertex(self, v: int, w: int):
        pass

    def add_edge(self, v: int, w: int):
        if self.validate_vertex(v) and self.validate_vertex(w):
            self._adj[v].append(w)
            if w in self._in_degree:
                self._in_degree[w] = self._in_degree[w] + 1
            else:
                self._in_degree[w] = 1
            self._E += 1
        else:
            raise Exception()

    def __len__(self):
        return self.no_of_edges()



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
            #Double header
            d = DAG(int(next(f)))
            d._V = int(next(f))
            for line in f:
                v = line.split(' ')
                d.add_edge(int(v[0]), int(v[1]))
        return d