import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertTrue(g.is_bipartite())
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())

    def test_03(self):
        g = Graph('test2.txt')
        self.assertEqual(g.get_vertex('v9'), None)
        g.add_vertex('v9')
        self.assertTrue('v9' in g.lis)
        g.add_edge('v8', 'v9')
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v6', 'v7', 'v8', 'v9'])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8', 'v9']])
        self.assertTrue('v9' in g.get_vertex('v8').adjacent_to)
        self.assertTrue('v8' in g.get_vertex('v9').adjacent_to)

if __name__ == '__main__':
   unittest.main()
