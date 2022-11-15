import unittest
from points import Point


class TestPoint(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Point(2, 3)), "(2, 3)")
        self.assertNotEqual(str(Point(3, 2)), "(2, 3)")

    def test_repr(self):
        self.assertEqual(repr(Point(2, 3)), "Point(2, 3)")
        self.assertNotEqual(repr(Point(3, 2)), "Point(2, 3)")

    def test_eq(self):
        self.assertTrue(Point(2, 3) == Point(2, 3))
        self.assertFalse(Point(2, 3) == Point(3, 2))

    def test_ne(self):
        self.assertTrue(Point(2, 3) != Point(3, 2))
        self.assertFalse(Point(2, 3) != Point(2, 3))

    def test_add(self):
        self.assertEqual(Point(3, 2) + Point(2, 3), Point(5, 5))
        self.assertNotEqual(Point(3, 2) + Point(2, 3), Point(5, 7))

    def test_sub(self):
        self.assertEqual(Point(2, 3) - Point(1, 1), Point(1, 2))
        self.assertNotEqual(Point(2, 3) - Point(1, 1), Point(3, 5))

    def test_mul(self):
        self.assertEqual(Point(2, 3) * Point(2, 2), 10)
        self.assertNotEqual(Point(2, 3) * Point(2, 2), 50)

    def test_cross(self):
        self.assertEqual(Point(2, 3).cross(Point(2, 1)), 4)
        self.assertNotEqual(Point(2, 3).cross(Point(2, 3)), 4)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertNotEqual(Point(2, 3).length(), 6)


if __name__ == '__main__':
    unittest.main()
