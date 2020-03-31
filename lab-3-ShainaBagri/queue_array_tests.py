import unittest
from queue_array import Queue

class TestLab3(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_is_empty(self):
        q = Queue(3)
        self.assertTrue(q.is_empty())
        q.enqueue(32)
        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertTrue(q.is_empty())
        q.enqueue(32)
        q.enqueue(16)
        q.enqueue(44)
        self.assertFalse(q.is_empty())

    def test_is_full(self):
        q = Queue(3, [4, 6, 22])
        q2 = Queue(2)
        self.assertFalse(q2.is_full())
        self.assertTrue(q.is_full())
        q.dequeue()
        self.assertFalse(q.is_full())
        q.enqueue(32)
        self.assertTrue(q.is_full())
        q2.enqueue(123)
        q2.enqueue(0)
        self.assertTrue(q2.is_full())

    def test_enqueue(self):
        q = Queue(3)
        q.enqueue(8)
        q.enqueue(42)
        self.assertEqual(q.num_items, 2)
        q.enqueue(76)
        self.assertEqual(q.items[0], 8)
        self.assertEqual(q.items[1], 42)
        self.assertEqual(q.items[2], 76)
        q.dequeue()
        self.assertEqual(q.rear, 0)
        q.enqueue(23)
        self.assertEqual(q.items[0], 23)
        self.assertTrue(q.is_full())
        self.assertEqual(q.front, 1)
        self.assertEqual(q.rear, 1)
        with self.assertRaises(IndexError):
            q.enqueue(1)

    def test_dequeue(self):
        q = Queue(3, [4, 6, 22])
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 6)
        self.assertEqual(q.num_items, 1)
        self.assertEqual(q.front, 2)
        q.enqueue(12)
        self.assertEqual(q.dequeue(), 22)
        self.assertEqual(q.front, 0)
        self.assertEqual(q.dequeue(), 12)
        self.assertTrue(q.is_empty())
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_size(self):
        q = Queue(4)
        q2 = Queue(3, [4, 6, 22])
        self.assertEqual(q.size(), 0)
        self.assertEqual(q2.size(), 3)
        q.enqueue(13)
        q2.dequeue()
        self.assertEqual(q.size(), 1)
        self.assertEqual(q2.size(), 2)

if __name__ == '__main__':
    unittest.main()
