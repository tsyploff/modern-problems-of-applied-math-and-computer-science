from random import randint
from typing import Tuple

from .extended_gcd import extended_gcd
from .prime_generator import prime_generator, power_mod


class RSA:

    def __init__(self, p: int, q: int):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)

    def generate_asymmetric_key_pair(self) -> Tuple[int, int]:
        open_exponent: int = randint(3, self.phi)
        gcd, (private_key, _) = extended_gcd(open_exponent, self.phi)
        while gcd != 1:
            open_exponent: int = randint(3, self.phi)
            gcd, (private_key, _) = extended_gcd(open_exponent, self.phi)
        return open_exponent, private_key

    def encrypt(self, message: int, open_exponent: int):
        return power_mod(message, open_exponent, self.n)

    @staticmethod
    def random_prime(n: int = 256, k: int = 10) -> int:
        return prime_generator(n, k)
