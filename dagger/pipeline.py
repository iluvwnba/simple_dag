from dagger.base import dag, vertex


def run() -> dag.DAG:
    t1, t2, t3, t4, t5, t6 = vertex.Vertex(v_id="t1"), vertex.Vertex(v_id="t2"), vertex.Vertex(v_id="t3"), \
                             vertex.Vertex(v_id="t4"), vertex.Vertex(v_id="t5"), vertex.Vertex(v_id="t6")
    with dag.DAG() as d:
        t1 >> t2 >> t4 >> t6
        t1 >> t3 >> t5
        t5 >> t6

    return d
