from dagger.base import dag,vertex


def run():
    d = dag.DAG()
    a, b, c = vertex.Vertex(v_id="a"), vertex.Vertex(v_id="b"), vertex.Vertex(v_id="c")
    d.add_edge(a, b)
    d.add_edge(b, c)
    d.add_edge(a, c)
    return d, d.check_cycle()


if __name__ == '__main__':
    run()
