import unittest
from dagger.base import dag , vertex

''''
TODO - Write tests after rewrite
'''


class TestDag(unittest.TestCase):

    def test_init(self):
        d = dag.GraphBase()
        a, b, c = vertex.Vertex(v_id="a"), vertex.Vertex(v_id="b"), vertex.Vertex(v_id="c")
        d.add_edge(a, b)
        d.add_edge(b, c)
        d.add_edge(a, c)
        self.assertTrue(len(d) == 3)

    def test_has_cycle(self):
        d = dag.DAG()
        a, b, c = vertex.Vertex(v_id="a"), vertex.Vertex(v_id="b"), vertex.Vertex(v_id="c")
        d.add_edge(a, b)
        d.add_edge(b, c)
        d.add_edge(a, c)
        self.assertFalse(d.check_cycle())

    def test_not_cycle(self):
        d = dag.DAG()
        a, b, c = vertex.Vertex(v_id="a"), vertex.Vertex(v_id="b"), vertex.Vertex(v_id="c")
        d.add_edge(a, b)
        d.add_edge(b, c)
        d.add_edge(c, a)
        self.assertTrue(d.check_cycle())

    def test_context_manager(self):
        t1, t2, t3, t4, t5, t6 = vertex.Vertex(v_id="t1"), vertex.Vertex(v_id="t2"), vertex.Vertex(v_id="t3"), \
                                 vertex.Vertex(v_id="t4"), vertex.Vertex(v_id="t5"), vertex.Vertex(v_id="t6")
        with dag.DAG() as d:
            t1 >> t2 >> t4 >> t6
            t1 >> t3 >> t5
            t5 >> t6
        self.assertTrue(len(d) == 6)

    def test_rshift_has_cycle(self):
        t1, t2, t3, t4, t5, t6 = vertex.Vertex(v_id="t1"), vertex.Vertex(v_id="t2"), vertex.Vertex(v_id="t3"), \
                                 vertex.Vertex(v_id="t4"), vertex.Vertex(v_id="t5"), vertex.Vertex(v_id="t6")
        with dag.DAG() as d:
            t1 >> t2 >> t4 >> t6
            t1 >> t3 >> t5
            t5 >> t6 >> t1
        self.assertTrue(d.check_cycle())

    def test_rshift_not_cycle(self):
        t1, t2, t3, t4, t5, t6 = vertex.Vertex(v_id="t1"), vertex.Vertex(v_id="t2"), vertex.Vertex(v_id="t3"), \
                                 vertex.Vertex(v_id="t4"), vertex.Vertex(v_id="t5"), vertex.Vertex(v_id="t6")
        with dag.DAG() as d:
            t1 >> t2 >> t4 >> t6
            t1 >> t3 >> t5
            t5 >> t6
        self.assertFalse(d.check_cycle())


if __name__ == '__main__':
    unittest.main()
