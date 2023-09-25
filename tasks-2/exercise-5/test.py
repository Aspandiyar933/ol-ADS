import unittest
from code import count_elements_in_range

class TestCountElementsInRange(unittest.TestCase):

    def test_count_elements(self):
        input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        a = 3
        b = 7
        expected_count = 5
        self.assertEqual(count_elements_in_range(input_array, a, b), expected_count)

    def test_empty_array(self):
        input_array = []
        a = 1
        b = 5
        expected_count = 0
        self.assertEqual(count_elements_in_range(input_array, a, b), expected_count)

    def test_no_elements_in_range(self):
        input_array = [10, 20, 30, 40, 50]
        a = 1
        b = 5
        expected_count = 0
        self.assertEqual(count_elements_in_range(input_array, a, b), expected_count)

    def test_all_elements_in_range(self):
        input_array = [2, 4, 6, 8, 10]
        a = 1
        b = 12
        expected_count = 5
        self.assertEqual(count_elements_in_range(input_array, a, b), expected_count)

if __name__ == '__main__':
    unittest.main()
