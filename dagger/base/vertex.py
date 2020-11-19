from __future__ import annotations
import uuid
import time
import subprocess


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
    def __init__(self, cmd: str, delay: int = 0, v_id: str = None, p_weight: int = 1):
        super(Operator, self).__init__(v_id=v_id)
        self._priority_weight: int = p_weight
        self._delay: int = delay
        self.cmd = cmd
    # Execution locker
    _lock_for_execution = False

    def is_running(self):
        return self._lock_for_execution

    def claim_lock(self):
        if self._lock_for_execution:
            OperatorException()
        self._lock_for_execution = True

    def release_lock(self):
        if not self._lock_for_execution:
            OperatorException()
        self._lock_for_execution = False

    def get_delay(self) -> int:
        return self._delay

    def run(self):
        pass


class BashOperator(Operator):
    def __init__(self, cmd: str, delay: int = 0, v_id: str = None, p_weight: int = 1):
        super(BashOperator, self).__init__(cmd, delay, v_id, p_weight)

    def run(self) -> None:
        """
            Execute DAG in sync
        """
        self.claim_lock()
        time.sleep(self.get_delay())
        out_b = subprocess.check_output([self.cmd])
        self.release_lock()
        print(out_b.decode('utf-8'))
        yield out_b.decode('utf-8')
