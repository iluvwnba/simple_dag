from dagger.base.dag import DAG
from dagger.base.vertex import Operator
import subprocess
import time


class BaseExecutor:
    def __init__(self, dag: DAG):
        self._dag = dag

    def execute(self) -> None:
        """
            Execute DAG in sync
        """
        opp: Operator
        for opp in self._dag.topological_order():
            opp.claim_lock()
            time.sleep(opp.get_delay())
            out_b = subprocess.check_output([opp.cmd])
            opp.release_lock()
            print(out_b.decode('utf-8'))
