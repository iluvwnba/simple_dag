from dagger.base.dag import DAG
from dagger.base.vertex import Operator

class BaseExecutor:
    def __init__(self, dag: DAG):
        self._dag = dag

    def execute(self) -> None:
        """
            Execute DAG in sync
        """
        pass


class LocalExecutor(BaseExecutor):
    #Turn into something a DAG can push too, execution queue
    def __init__(self, dag: DAG):
        super().__init__(dag)
        self._execution_ops = dag.topological_order()

    def execute(self):
        while self._execution_ops:
            op = self._execution_ops.popleft()
            try:
                op: Operator
                next(op.run())
            except StopIteration:
                pass