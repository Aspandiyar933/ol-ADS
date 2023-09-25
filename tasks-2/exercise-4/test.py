import unittest
from code import separate_even_odd

class TestSeparateEvenOdd(unittest.TestCase):

    def test_separate(self):
        input_array = [1, 2, 3, 4, 5, 6]
        expected_result = [1, 3, 5, 2, 4, 6]
        self.assertEqual(separate_even_odd(input_array), expected_result)

    def test_empty_array(self):
        input_array = []
        expected_result = []
        self.assertEqual(separate_even_odd(input_array), expected_result)

    def test_single_element(self):
        input_array = [42]
        expected_result = [42]
        self.assertEqual(separate_even_odd(input_array), expected_result)

if __name__ == '__main__':
    unittest.main()
