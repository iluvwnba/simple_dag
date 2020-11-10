import unittest
import dagger.base.dag as dag

''''
TODO - Write tests after rewrite
'''


class TestDag(unittest.TestCase):

    def test_init(self):
        d = dag.DAG(1)
        self.assertTrue(len(d) == 1)

if __name__ == '__main__':
    unittest.main()
