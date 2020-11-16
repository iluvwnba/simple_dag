from __future__ import annotations
import uuid
import subprocess
import time


class OperatorException(Exception):
    pass


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
    def __init__(self, delay: int = 0, v_id: str = None, p_weight: int = 1):
        super(Operator, self).__init__(v_id=v_id)
        self._priority_weight: int = p_weight
        self._delay: int = delay
    # Execution locker
    _lock_for_execution = False

    def execute(self):
        pass


class BashOperator(Operator):
    def __init__(self, cmd: str, delay: int = 0, v_id: str = None, p_weight: int = 1):
        super(BashOperator, self).__init__(delay, v_id, p_weight)
        self.cmd: str = cmd

    def is_running(self):
        return self._lock_for_execution

    def execute(self) -> str:
        if self.is_running():
            raise OperatorException()
        self._lock_for_execution = True
        # Do stuff faking delay
        time.sleep(self._delay)
        out_b = subprocess.check_output([self.cmd])
        out_t: str = out_b.decode('utf-8')

        # Completed execution for the job
        self._lock_for_execution = False

        return out_t
