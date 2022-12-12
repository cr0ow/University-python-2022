import unittest
from random_queue import RandomQueue


class TestPoint(unittest.TestCase):

    def test_is_empty(self):
        queue = RandomQueue()
        self.assertEqual(True, queue.is_empty())

    def test_is_full(self):
        queue = RandomQueue()
        for i in range(5):
            queue.insert(1)
        self.assertEqual(True, queue.is_full())

    def test_insert(self):
        queue = RandomQueue()
        queue.insert(5)
        self.assertEqual(1, queue.size)
        self.assertEqual(5, queue.remove())

    def test_remove(self):
        queue = RandomQueue()
        for i in range(5):
            queue.insert(i)
        for i in range(5):
            queue.remove()
        self.assertEqual(0, queue.size)


if __name__ == '__main__':
    unittest.main()
