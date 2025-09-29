import unittest
from arrays import invert_array, bubble_sort, find_min, find_max, sum_array, average_array, count_occurrences

class TestArrayFunctions(unittest.TestCase):
    def test_invert_array(self):
        self.assertEqual(invert_array([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(invert_array([7, 8, 9]), [9, 8, 7])
        self.assertEqual(invert_array([1]), [1])
        self.assertEqual(invert_array([3]), [3])

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([4, 2, 7, 1]), [1, 2, 4, 7])
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(bubble_sort([5]), [5])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([9, 9, 9]), [9, 9, 9])

    def test_find_min(self):
        self.assertEqual(find_min([4, 2, 7, 1]), 1)
        self.assertEqual(find_min([10, -5, 0, 12]), -5)
        self.assertEqual(find_min([100]), 100)

    def test_find_max(self):
        self.assertEqual(find_max([4, 2, 7, 1]), 7)
        self.assertEqual(find_max([10, -5, 0, 12]), 12)
        self.assertEqual(find_max([100]), 100)

    def test_sum_array(self):
        self.assertEqual(sum_array([1, 2, 3, 4]), 10)
        self.assertEqual(sum_array([0, 0, 0]), 0)
        self.assertEqual(sum_array([-1, 1]), 0)
        self.assertEqual(sum_array([1]), 1)

    def test_average_array(self):
        self.assertEqual(average_array([1, 2, 3, 4]), 2.5)
        self.assertEqual(average_array([10, 20, 30]), 20)
        self.assertEqual(average_array([0, 0, 0]), 0)
        self.assertEqual(average_array([-1, 1]), 0)

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences([1, 2, 3, 4, 2], 2), 2)
        self.assertEqual(count_occurrences([1, 1, 1], 1), 3)
        self.assertEqual(count_occurrences([1, 2, 3], 4), 0)
        self.assertEqual(count_occurrences([1], 1), 1)

if __name__ == '__main__':
    unittest.main()