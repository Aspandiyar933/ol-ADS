import unittest
from code import separate_positive_negative

class TestSeparatePositiveNegative(unittest.TestCase):

    def test_separate(self):
        input_array = [3, -2, 1, -4, 0, 5, -7]
        expected_result = [3, 1, 0, 5, -2, -4, -7]
        self.assertEqual(separate_positive_negative(input_array), expected_result)

    def test_empty_array(self):
        input_array = []
        expected_result = []
        self.assertEqual(separate_positive_negative(input_array), expected_result)

    def test_only_negative(self):
        input_array = [-1, -2, -3, -4]
        expected_result = [-1, -2, -3, -4]
        self.assertEqual(separate_positive_negative(input_array), expected_result)

    def test_only_positive(self):
        input_array = [1, 2, 3, 4]
        expected_result = [1, 2, 3, 4]
        self.assertEqual(separate_positive_negative(input_array), expected_result)

if __name__ == '__main__':
    unittest.main()
