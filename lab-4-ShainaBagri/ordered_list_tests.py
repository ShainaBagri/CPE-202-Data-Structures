import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertEqual(t_list.size(), 0)
        self.assertEqual(t_list.python_list_reversed(), [])
        self.assertFalse(t_list.search(10))
        self.assertEqual(t_list.index(10), None)
        self.assertFalse(t_list.remove(10))
        with self.assertRaises(IndexError):
            t_list.pop(0)
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
        t_list.add(15)
        t_list.add(20)
        t_list.add(3)
        t_list.add(47)
        t_list.add(18)
        self.assertEqual(t_list.size(), 5)
        t_list.add(20)
        self.assertEqual(t_list.size(), 5)
        self.assertEqual(t_list.python_list(), [3, 15, 18, 20, 47])
        self.assertEqual(t_list.python_list_reversed(), [47, 20, 18, 15, 3])
        self.assertTrue(t_list.search(18))
        self.assertTrue(t_list.search(3))
        self.assertTrue(t_list.search(47))
        self.assertFalse(t_list.search(21))
        self.assertEqual(t_list.index(18), 2)
        self.assertEqual(t_list.index(3), 0)
        self.assertEqual(t_list.index(47), 4)
        self.assertEqual(t_list.index(21), None)
        self.assertTrue(t_list.remove(18))
        self.assertEqual(t_list.python_list(), [3, 15, 20, 47])
        self.assertTrue(t_list.remove(3))
        self.assertTrue(t_list.remove(47))
        self.assertFalse(t_list.remove(10))
        self.assertEqual(t_list.python_list_reversed(), [20, 15])
        self.assertEqual(t_list.size(), 2)
        with self.assertRaises(IndexError):
            t_list.pop(-1)
        with self.assertRaises(IndexError):
            t_list.pop(2)
        with self.assertRaises(IndexError):
            t_list.pop(3)
        t_list.add(3)
        t_list.add(47)
        t_list.add(18)
        self.assertEqual(t_list.pop(2), 18)
        self.assertEqual(t_list.pop(0), 3)
        self.assertEqual(t_list.pop(2), 47)



if __name__ == '__main__': 
    unittest.main()
