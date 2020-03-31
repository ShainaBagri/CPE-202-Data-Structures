import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertFalse(bst.search(32))
        self.assertEqual(bst.find_min(), None)
        self.assertEqual(bst.find_max(), None)
        self.assertEqual(bst.tree_height(), None)
        self.assertEqual(bst.inorder_list(), [])
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.level_order_list(), [])
        bst.insert(10, 'stuff')
        self.assertFalse(bst.is_empty())
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.preorder_list(), [10])
        bst.insert(5, 'a')
        bst.insert(14, 'b')
        bst.insert(2, 'c')
        bst.insert(8, 'd')
        bst.insert(20, 'e')
        self.assertTrue(bst.search(8))
        self.assertFalse(bst.search(19))
        self.assertEqual(bst.find_min(), (2, 'c'))
        self.assertEqual(bst.find_max(), (20, 'e'))
        self.assertEqual(bst.tree_height(), 2)
        self.assertEqual(bst.inorder_list(), [2, 5, 8, 10, 14, 20])
        self.assertEqual(bst.preorder_list(), [10, 5, 2, 8, 14, 20])
        self.assertEqual(bst.level_order_list(), [10, 5, 14, 2, 8, 20])

if __name__ == '__main__': 
    unittest.main()
