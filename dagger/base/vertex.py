from __future__ import annotations

from dagger.base.dag import DAG

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

'''
Known
TODO Will be rewitten to work with new DAG.py
Questions
'''


class Vertex:
    def __init__(self, v_id: int, dag: DAG):
        self.v_id: int = v_id
        self.dag = dag

    def __key(self):
        return (self.v_id)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        # Are they the same type or have the same id
        if isinstance(other, Vertex):
            return self.__key() == other.__key()
        return NotImplemented

    def set_dag(self, d: DAG):
        # Replace with @property and @setter annotations
        # check if exists
        self.dag = d

    def get_vertex_id(self) -> int:
        return self.v_id

    def set_downstream(self, v: Vertex):
        pass

    def set_upstream(self, v: Vertex):
        pass

    # Do we need a list return version of this
    def get_upstream(self) -> Vertex:
        pass

    def get_downstream(self) -> Vertex:
        pass

    def execute(self):
        pass
