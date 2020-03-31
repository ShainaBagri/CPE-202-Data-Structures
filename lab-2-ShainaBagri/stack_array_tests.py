import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

    def test_init(self):
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_repr(self):
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    def test_is_empty(self):
        stack1 = Stack(5)
        stack2 = Stack(3, [8, 12, 52])
        self.assertTrue(stack1.is_empty())
        self.assertFalse(stack2.is_empty())
        stack1.push(5)
        self.assertFalse(stack1.is_empty())

    def test_is_full(self):
        stack1 = Stack(2)
        stack2 = Stack(3, [8, 12, 52])
        self.assertFalse(stack1.is_full())
        self.assertTrue(stack2.is_full())
        stack1.push(5)
        self.assertFalse(stack1.is_full())
        stack1.push(99)
        self.assertTrue(stack1.is_full())

    def test_push(self):
        stack = Stack(4)
        stack.push(2)
        stack.push(16)
        self.assertEqual(stack.num_items, 2)
        stack.push(10)
        stack.push(21)
        self.assertEqual(stack.items[0], 2)
        self.assertEqual(stack.items[1], 16)
        self.assertEqual(stack.items[2], 10)
        self.assertEqual(stack.items[3], 21)
        self.assertTrue(stack.is_full())
        with self.assertRaises(IndexError):  # used to check for exception
            stack.push(66)

    def test_pop(self):
        stack = Stack(3, [8, 12, 52])
        self.assertEqual(stack.pop(), 52)
        self.assertEqual(stack.pop(), 12)
        self.assertEqual(stack.num_items, 1)
        self.assertEqual(stack.pop(), 8)
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):  # used to check for exception
            stack.pop()

    def test_peek(self):
        stack = Stack(3, [8, 12, 52])
        self.assertEqual(stack.peek(), 52)
        self.assertEqual(stack.num_items, 3)
        self.assertEqual(stack.peek(), 52)
        stack.pop()
        self.assertEqual(stack.peek(), 12)
        stack.pop()
        self.assertEqual(stack.peek(), 8)
        stack.pop()
        with self.assertRaises(IndexError):  # used to check for exception
            stack.peek()

    def test_size(self):
        stack1 = Stack(5)
        stack2 = Stack(3, [8, 12, 52])
        self.assertEqual(stack1.size(), 0)
        self.assertEqual(stack2.size(), 3)
        stack1.push(5)
        self.assertEqual(stack1.size(), 1)
        stack2.pop()
        self.assertEqual(stack2.size(), 2)

if __name__ == '__main__': 
    unittest.main()
