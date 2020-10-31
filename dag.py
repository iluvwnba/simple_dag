from __future__ import annotations
from vertex import Vertex

'''
Known
Each point is called a vertex
Questions
Do you just store a dictionary of task_ids, vertexs
Is a DAG a namespace thats gets sorted at runtime to understand running order -
    Do vertexs just manage there own dependents
ACII tree view implementation

'''
class DAG:

    def __init__(self, dag_id:str):
        self.dag_id:str = dag_id
        self.task_count:int = 0

    def __repr__(self):
        pass

    def __ne__(self, other):
        pass

    def add_vertex(self, vertex:Vertex):
        pass

    def run(self):
        pass


