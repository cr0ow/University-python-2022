import unittest
from rectangles import Rectangle, from_points
from points import Point


class TestRectangle(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Rectangle(2, 3, 4, 5)), "[(2, 3), (4, 5)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(2, 3, 4, 5)), "Rectangle(2, 3, 4, 5)")

    def test_eq(self):
        self.assertTrue(Rectangle(2, 3, 4, 5) == Rectangle(2, 3, 4, 5))
        self.assertFalse(Rectangle(2, 3, 5, 5) == Rectangle(2, 3, 4, 5))

    def test_ne(self):
        self.assertFalse(Rectangle(2, 3, 4, 5) != Rectangle(2, 3, 4, 5))
        self.assertTrue(Rectangle(2, 3, 5, 5) != Rectangle(2, 3, 4, 5))

    def test_center(self):
        self.assertEqual(Rectangle(2, 3, 4, 5).center(), Point(3, 4))

    def test_area(self):
        self.assertEqual(Rectangle(2, 3, 4, 5).area(), 4)

    def test_move(self):
        r = Rectangle(2, 3, 4, 5).move(3, 3)
        self.assertTrue(r == Rectangle(5, 6, 7, 8))

    def test_from_points(self):
        r1 = from_points((Point(1, 1), Point(4, 4)))
        r2 = Rectangle(1, 1, 4, 4)
        self.assertEqual(r2, r1)


if __name__ == '__main__':
    unittest.main()
