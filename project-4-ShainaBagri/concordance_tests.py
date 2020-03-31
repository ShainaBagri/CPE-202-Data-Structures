import unittest
import filecmp
import subprocess
from concordance import *

use_diff = False

class TestList(unittest.TestCase):

    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        if use_diff:
            err = subprocess.call("diff -wb file1_con.txt file1_sol.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        if use_diff:
            err = subprocess.call("diff -wb file2_con.txt file2_sol.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        if use_diff:
            err = subprocess.call("diff -wb declaration_con.txt declaration_sol.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

    def test_04(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("empty.txt")
        conc.write_concordance("empty_con.txt")
        if use_diff:
            err = subprocess.call("diff -wb empty_con.txt empty_sol.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("empty_con.txt", "empty_sol.txt"))

    def test_05(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("onlystop.txt")
        conc.write_concordance("onlystop_con.txt")
        if use_diff:
            err = subprocess.call("diff -wb onlystop_con.txt onlystop_sol.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("onlystop_con.txt", "onlystop_sol.txt"))

if __name__ == '__main__':
   unittest.main()
