from dagger.base import vertex, dag


def run():
    '''
    No longer works after rewrite
    TODO DO new example
    '''
    d = dag.DAG("dag")
    v_1 = vertex.Vertex(1, d)
    v_2 = vertex.Vertex(5, d)
    d.add_vertex(v_1)
    d.add_vertex(v_2)
    print(d.topological_sort(d))


if __name__ == '__main__':
    run()
