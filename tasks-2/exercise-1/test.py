import unittest
from code import check_weight_limit

import unittest

class TestCheckWeightLimit(unittest.TestCase):

    def test_total_weight_less_than_capacity(self):
        items = [100, 200, 300]
        capacity = 1000
        self.assertTrue(check_weight_limit(items, capacity))

    def test_total_weight_equal_to_capacity(self):
        items = [100, 200, 300]
        capacity = 600
        self.assertTrue(check_weight_limit(items, capacity))

    def test_total_weight_greater_than_capacity(self):
        items = [100, 200, 300]
        capacity = 400
        self.assertFalse(check_weight_limit(items, capacity))

    def test_empty_items(self):
        items = []
        capacity = 1000
        self.assertTrue(check_weight_limit(items, capacity))

if __name__ == '__main__':
    unittest.main()
