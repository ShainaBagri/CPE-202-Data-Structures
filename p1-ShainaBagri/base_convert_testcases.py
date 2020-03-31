import unittest
from  base_convert import *

# Starter test cases - write more!

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")

    def test_base10(self):
        self.assertEqual(convert(2057,10), "2057")

    def test_base7(self):
        self.assertEqual(convert(62,7), "116")

    def test_base13(self):
        self.assertEqual(convert(487,13), "2B6")

if __name__ == "__main__":
        unittest.main()