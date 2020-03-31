import unittest
from stack_linked import *
        
class TestLab2(unittest.TestCase):

    def test_node_init(self):
        node1 = Node(1)
        self.assertEqual(node1.data, 1)
        self.assertEqual(node1.next, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.data, 2)
        self.assertEqual(node2.next, node1)

    def test_node_eq(self):
        node1a = Node(1)
        node1b = Node(1)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3)
        self.assertNotEqual(node1a, node1b)

    def test_node_repr(self):
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self):
        stack = Stack(5)
        self.assertEqual(stack.top, None)
        self.assertEqual(stack.capacity, 5)

        init_stack = Node(2, Node(1, None))
        stack = Stack(5, init_stack)
        self.assertEqual(stack.top, init_stack)
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, Node(6, Node(5, Node(4, Node(3, Node(2, Node(1, None)))))))

    def test_stack_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(5, init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_stack_repr(self):
        init_stack = Node(2, Node(1, None))
        stack = Stack(5, init_stack)
        self.assertEqual(stack.__repr__(), "Stack(5, Node(2, Node(1, None)))")

    def test_is_empty(self):
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        stack.push(3)
        self.assertFalse(stack.is_empty())
        stack.pop()
        self.assertTrue(stack.is_empty())
        init_stack = Node(2, Node(1, None))
        stack2 = Stack(4, init_stack)
        self.assertFalse(stack2.is_empty())
        stack3 = Stack(2, init_stack)
        self.assertFalse(stack3.is_empty())

    def test_is_full(self):
        stack = Stack(3)
        self.assertFalse(stack.is_full())
        stack.push(3)
        stack.push(6)
        self.assertFalse(stack.is_full())
        stack.push(52)
        self.assertTrue(stack.is_full())
        stack.pop()
        self.assertFalse(stack.is_full())
        init_stack = Node(2, Node(1, None))
        stack2 = Stack(2, init_stack)
        self.assertTrue(stack2.is_full())

    def test_push(self):
        stack = Stack(4)
        stack.push(2)
        self.assertEqual(stack.top.data, 2)
        stack.push(16)
        self.assertEqual(stack.num_items, 2)
        self.assertEqual(stack.top.data, 16)
        stack.push(10)
        self.assertEqual(stack.top.data, 10)
        stack.push(21)
        self.assertEqual(stack.top.data, 21)
        self.assertTrue(stack.is_full())
        with self.assertRaises(IndexError):  # used to check for exception
            stack.push(66)

    def test_pop(self):
        init_stack = Node(2, Node(1, Node(52, None)))
        stack = Stack(3, init_stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.num_items, 1)
        self.assertEqual(stack.pop(), 52)
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):  # used to check for exception
            stack.pop()

    def test_peek(self):
        init_stack = Node(2, Node(1, Node(52, None)))
        stack = Stack(3, init_stack)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.num_items, 3)
        self.assertEqual(stack.peek(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)
        stack.pop()
        self.assertEqual(stack.peek(), 52)
        stack.pop()
        with self.assertRaises(IndexError):  # used to check for exception
            stack.peek()

    def test_size(self):
        stack1 = Stack(5)
        init_stack = Node(2, Node(1, Node(52, None)))
        stack2 = Stack(3, init_stack)
        self.assertEqual(stack1.size(), 0)
        self.assertEqual(stack2.size(), 3)
        stack1.push(5)
        self.assertEqual(stack1.size(), 1)
        stack2.pop()
        self.assertEqual(stack2.size(), 2)

if __name__ == '__main__': 
    unittest.main()
