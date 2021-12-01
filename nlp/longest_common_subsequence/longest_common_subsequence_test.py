import unittest
from . import common_prefix, longest_common_subsequence


class LongestCommonSubsequenceTest(unittest.TestCase):
    def test_common_prefix(self):
        self.assertEqual(common_prefix("abc", "abc"), "abc")
        self.assertEqual(common_prefix("abc", "abcde"), "abc")
        self.assertEqual(common_prefix("abc", "sabcde"), "")

    def test_longest_common_subsequence(self):
        self.assertEqual(longest_common_subsequence("abc", "abc"), "abc")
        self.assertEqual(longest_common_subsequence("abc", "abcde"), "abc")
        self.assertEqual(longest_common_subsequence("abc", "sabcde"), "abc")
        self.assertEqual(longest_common_subsequence("abc", "def"), "")


if __name__ == '__main__':
    unittest.main()
