import unittest
from base import dag
from base import vertex

class TestDag(unittest.TestCase):

    def test_init(self):
        d = dag.DAG("dag_one")
        self.assertTrue(d.dag_id == "dag_one")
        self.assertTrue(len(d) == 0)

    def test_add_vertex(self):
        d = dag.DAG("adder_dag")
        d.add_vertex(vertex.Vertex(1, self))

if __name__ == '__main__':
    unittest.main()
