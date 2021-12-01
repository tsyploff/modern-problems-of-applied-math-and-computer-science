import unittest
from . import levenshtein_distance


class LevenshteinDistanceTest(unittest.TestCase):
    def test_levenshtein_distance(self):
        self.assertEqual(levenshtein_distance("abc", "abc"), 0)
        self.assertEqual(levenshtein_distance("abc", "abcde"), 2)
        self.assertEqual(levenshtein_distance("abc", "sabcde"), 3)


if __name__ == '__main__':
    unittest.main()
