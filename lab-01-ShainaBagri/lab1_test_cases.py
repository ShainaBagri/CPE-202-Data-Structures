# CPE 202 Lab 1 Test Cases

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        tlist1 = [4, 19, 13]
        self.assertEqual(max_list_iter(tlist1), 19)
        tlist2 = []
        self.assertEqual(max_list_iter(tlist2), None)
        tlist3 = [5, 5, 5]
        self.assertEqual(max_list_iter(tlist3), 5)
        tlist4 = [-3, -10, -9]
        self.assertEqual(max_list_iter(tlist4), -3)

    def test_reverse_rec(self):
        lis = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(lis)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([5, 10]), [10, 5])
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([-1, 16, 3]), [3, 16, -1])

    def test_bin_search(self):
        lis = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(0, 0, 0, lis)
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4)
        self.assertEqual(bin_search(10, low, high, list_val), 8)
        self.assertEqual(bin_search(0, low, high, list_val), 0)
        self.assertEqual(bin_search(8, low, high, list_val), 6)
        list_val2 = [0, 2, 4, 8, 10, 16]
        high2 = len(list_val2) - 1
        self.assertEqual(bin_search(8, low, high2, list_val2), 3)
        self.assertEqual(bin_search(2, low, high2, list_val2), 1)
        list_val3 = [1, 3, 3, 3, 3]
        high3 = len(list_val3) - 1
        self.assertEqual(bin_search(3, low, high3, list_val3), 2)



if __name__ == "__main__":
        unittest.main()

