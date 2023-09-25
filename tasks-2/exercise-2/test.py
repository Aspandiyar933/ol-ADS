import unittest
from code import check_qualification

class TestCheckQualification(unittest.TestCase):

    def test_qualifies(self):
        scores = [80, 90, 85, 88, 92, 78, 89, 91, 87, 84]
        threshold = 800
        self.assertTrue(check_qualification(scores, threshold))

    def test_does_not_qualify(self):
        scores = [70, 75, 68, 72, 80, 79, 63, 68, 71, 74]
        threshold = 800
        self.assertFalse(check_qualification(scores, threshold))

    def test_empty_scores(self):
        scores = []
        threshold = 800
        self.assertFalse(check_qualification(scores, threshold))

if __name__ == '__main__':
    unittest.main()
