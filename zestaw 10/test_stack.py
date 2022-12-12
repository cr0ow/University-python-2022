import unittest
from stack import Stack


class TestPoint(unittest.TestCase):

    def test_is_empty(self):
        stack = Stack()
        self.assertEqual(True, stack.is_empty())

    def test_is_full(self):
        stack = Stack()
        for i in range(5):
            stack.push(1)
        self.assertEqual(True, stack.is_full())

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.size)
        for i in range(4):
            stack.push(1)
        self.assertRaises(ValueError, lambda: stack.push(1))

    def test_pop(self):
        stack = Stack()
        for i in range(5):
            stack.push(1)
        stack.pop()
        self.assertEqual(4, stack.size)
        for i in range(4):
            stack.pop()
        self.assertRaises(ValueError, lambda: stack.pop())


if __name__ == '__main__':
    unittest.main()
