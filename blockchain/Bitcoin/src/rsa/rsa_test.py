import unittest

from .extended_gcd import extended_gcd
from .prime_generator import (
    eratosthenes_sieve,
    power_mod,
    lucas_lehmer_primality_test,
    mersenne_generator,
)


class RSATest(unittest.TestCase):
    def setUp(self) -> None:
        self.mersennes = [
            3,
            7,
            31,
            127,
            8191,
            131071,
            524287,
            2147483647,
            2305843009213693951,
        ]

    def test_eratosthenes_sieve(self):
        self.assertListEqual(eratosthenes_sieve(25), [2, 3, 5, 7, 11, 13, 17, 19, 23])
        self.assertListEqual(eratosthenes_sieve(23), [2, 3, 5, 7, 11, 13, 17, 19, 23])
        self.assertListEqual(eratosthenes_sieve(10), [2, 3, 5, 7])

    def test_power_mod(self):
        self.assertEqual(power_mod(595, 703, 991), 342)
        self.assertEqual(power_mod(21, 13, 2 ** 256), 154472377739119461)

    def test_extended_gcd(self):
        self.assertEqual(extended_gcd(19, 32), (1, (-5, 3)))
        self.assertEqual(extended_gcd(32, 19), (1, (3, -5)))
        self.assertEqual(
            extended_gcd(614513514531, 315134148), (21, (-7230837, 14100176341))
        )

    def test_lucas_lehmer(self):
        self.assertTrue(lucas_lehmer_primality_test(2))
        self.assertTrue(lucas_lehmer_primality_test(3))
        self.assertTrue(lucas_lehmer_primality_test(5))
        self.assertTrue(lucas_lehmer_primality_test(7))
        self.assertTrue(lucas_lehmer_primality_test(13))
        self.assertTrue(lucas_lehmer_primality_test(17))
        self.assertTrue(lucas_lehmer_primality_test(19))
        self.assertTrue(lucas_lehmer_primality_test(31))
        self.assertTrue(lucas_lehmer_primality_test(61))
        self.assertFalse(lucas_lehmer_primality_test(23))
        self.assertFalse(lucas_lehmer_primality_test(29))

    def test_mersenne_generator(self):
        self.assertListEqual(mersenne_generator(65), self.mersennes)


if __name__ == "__main__":
    unittest.main()
