from __future__ import annotations
from base import vertex
from collections import OrderedDict

class DAGError(Exception):
    print("DagError: {}".format(Exception))
    pass

'''
Known
OrderedDict is used to store all the vertex, top sort with ensure that they are
    DAG
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
        self.reset_dag()

    def reset_dag(self):
        self.dag = OrderedDict()

    def __repr__(self):
        pass

    def __ne__(self, other):
        pass

    def add_vertex(self, vertex:Vertex, dag=None):
        if not dag:
            dag = self.dag
        if vertex in dag:
           raise DAGError("Vertex already exists")
        dag[vertex.get_vertex_id()] = vertex

    def __len__(self):
        return len(self.dag)
