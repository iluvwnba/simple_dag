import unittest
import dagger.base.dag as dag

''''
TODO - Write tests after rewrite
'''


class TestDag(unittest.TestCase):

    def test_init(self):
        d = dag.GraphBase()
        a, b, c = dag.Vertex(v_id="a"), dag.Vertex(v_id="b"), dag.Vertex(v_id="c")
        d.add_edge(a, b)
        d.add_edge(b, c)
        d.add_edge(a, c)
        self.assertTrue(len(d) == 3)

    def test_has_cycle(self):
        d = dag.DAG()
        a, b, c = dag.Vertex(v_id="a"), dag.Vertex(v_id="b"), dag.Vertex(v_id="c")
        d.add_edge(a, b)
        d.add_edge(b, c)
        d.add_edge(a, c)
        self.assertFalse(d.check_cycle())

    def test_not_cycle(self):
        d = dag.DAG()
        a, b, c = dag.Vertex(v_id="a"), dag.Vertex(v_id="b"), dag.Vertex(v_id="c")
        d.add_edge(a, b)
        d.add_edge(b, c)
        d.add_edge(c, a)
        self.assertTrue(d.check_cycle())


if __name__ == '__main__':
    unittest.main()
