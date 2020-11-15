from __future__ import annotations
import uuid


class Vertex:
    def __init__(self, v_id: str = None):
        if v_id:
            self.id = v_id
        else:
            # Validate is unique
            self.id: str = str(uuid.uuid4())[:4]

    def __repr__(self):
        return self.id

    def __rshift__(self, other: Vertex):
        from dagger.base.dag import DagContext
        DagContext.get_current_dag().add_edge(self, other)
        return other


class Operator(Vertex):
    def __init__(self, v_id: str = None):
        super(Operator, self).__init__(v_id=v_id)
