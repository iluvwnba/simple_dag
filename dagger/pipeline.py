from dagger.base import dag


def run():
    d = dag.DAG()
    a, b, c = dag.Vertex(v_id="a"), dag.Vertex(v_id="b"), dag.Vertex(v_id="c")
    d.add_edge(a, b)
    d.add_edge(b, c)
    d.add_edge(a, c)
    print(d.check_cycle())


if __name__ == '__main__':
    run()
