# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        try:
            postfix_eval("6 4 / 2 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid bitshift operation")

    def test_postfix_eval_06(self):
        self.assertAlmostEqual(postfix_eval("9.5 2.5 + 3 / 5 + 20 2 - 3 / *"), 54)

    def test_postfix_eval_07(self):
        self.assertAlmostEqual(postfix_eval("3 5 + 3 **"), 512)

    def test_postfix_eval_08(self):
        with self.assertRaises(ValueError):
            postfix_eval("3 4 * 2 2 - /")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("( 1 + ( 2 - 3 ) ) * 8"), "1 2 3 - + 8 *")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("<< 11 5"), "11 5 <<")
        self.assertEqual(prefix_to_postfix("/ + 2 4 + 6 8"), "2 4 + 6 8 + /")


if __name__ == "__main__":
    unittest.main()
