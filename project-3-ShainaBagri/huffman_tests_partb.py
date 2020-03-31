import unittest
import filecmp
import subprocess
from huffman import *

usediff = False  # When comparing files: True to use Linux diff, False to use Python filecmp

class TestList(unittest.TestCase):
   def test_parse_header(self):
      header = "97 2 98 4 99 8 100 16 102 2"
      freqlist = parse_header(header)
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0]
      self.assertListEqual(freqlist[97:104], anslist[97:104])

   def test_decode_01(self):
      huffman_decode("file1_soln.txt", "file1_decode.txt")
      # detect errors by comparing your encoded file with a *known* solution file
      if usediff:
         err = subprocess.call("diff -wb file1.txt file1_decode.txt", shell=True)
         self.assertEqual(err, 0)
      else:
         self.assertTrue(filecmp.cmp("file1.txt", "file1_decode.txt"))

   def test_decode_02(self):
      huffman_decode("declaration_soln.txt", "declaration_decode.txt")
      # detect errors by comparing your encoded file with a *known* solution file
      if usediff:
         err = subprocess.call("diff -wb declaration.txt declaration_decode.txt", shell=True)
         self.assertEqual(err, 0)
      else:
         self.assertTrue(filecmp.cmp("declaration.txt", "declaration_decode.txt"))

   def test_decode_03(self):
      huffman_decode("multiline_soln.txt", "multiline_decode.txt")
      # detect errors by comparing your encoded file with a *known* solution file
      if usediff:
         err = subprocess.call("diff -wb multiline.txt multiline_decode.txt", shell=True)
         self.assertEqual(err, 0)
      else:
         self.assertTrue(filecmp.cmp("multiline.txt", "multiline_decode.txt"))

   def test_decode_04(self):
      huffman_decode("onechar_soln.txt", "onechar_decode.txt")
      # detect errors by comparing your encoded file with a *known* solution file
      if usediff:
         err = subprocess.call("diff -wb onechar.txt onechar_decode.txt", shell=True)
         self.assertEqual(err, 0)
      else:
         self.assertTrue(filecmp.cmp("onechar.txt", "onechar_decode.txt"))

   def test_decode_05(self):
      huffman_decode("empty_soln.txt", "empty_decode.txt")
      # detect errors by comparing your encoded file with a *known* solution file
      if usediff:
         err = subprocess.call("diff -wb empty.txt empty_decode.txt", shell=True)
         self.assertEqual(err, 0)
      else:
         self.assertTrue(filecmp.cmp("empty.txt", "empty_decode.txt"))

if __name__ == '__main__':
   unittest.main()
