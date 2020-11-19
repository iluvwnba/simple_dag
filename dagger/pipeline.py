from dagger.base import dag, vertex, executor


def run() -> dag.DAG:
    t1, t2 = vertex.BashOperator(v_id="t1", cmd="ls", delay=5), vertex.BashOperator(v_id="t2", cmd="ls")
    with dag.DAG() as d:
        t1 >> t2

    e = executor.LocalExecutor(d)
    e.execute()

    return d
