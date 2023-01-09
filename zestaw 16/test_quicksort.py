import unittest
import generator as gen
import quicksort as quick

size = 100


class TestQuicksort(unittest.TestCase):

    def test_sort_with_random(self):
        to_sort = gen.random(size)
        quick.quicksort(to_sort, 0, len(to_sort) - 1, quick.compare)
        for i in range(len(to_sort) - 1):
            self.assertNotEqual(1, quick.compare(to_sort[i], to_sort[i+1]))

    def test_sort_with_almost_sorted(self):
        to_sort = gen.almost_sorted(size)
        quick.quicksort(to_sort, 0, len(to_sort) - 1, quick.compare)
        for i in range(len(to_sort) - 1):
            self.assertNotEqual(1, quick.compare(to_sort[i], to_sort[i+1]))

    def test_sort_with_almost_sorted_reverted(self):
        to_sort = gen.almost_sorted_reverted(size)
        quick.quicksort(to_sort, 0, len(to_sort) - 1, quick.compare)
        for i in range(len(to_sort) - 1):
            self.assertNotEqual(1, quick.compare(to_sort[i], to_sort[i + 1]))

    def test_sort_with_random_gauss(self):
        to_sort = gen.random_gauss(size)
        quick.quicksort(to_sort, 0, len(to_sort) - 1, quick.compare)
        for i in range(len(to_sort) - 1):
            self.assertNotEqual(1, quick.compare(to_sort[i], to_sort[i+1]))

    def test_sort_with_random_from_set(self):
        to_sort = gen.random_from_set(size)
        quick.quicksort(to_sort, 0, len(to_sort) - 1, quick.compare)
        for i in range(len(to_sort) - 1):
            self.assertNotEqual(1, quick.compare(to_sort[i], to_sort[i+1]))


if __name__ == '__main__':
    unittest.main()
