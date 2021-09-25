from typing import Tuple


def extended_gcd(a: int, b: int) -> Tuple[int, Tuple[int, int]]:
    """
    Возвращает НОД(a, b) и числа c, d, такие, что
    a*c + b*d = НОД(a, b)
    """
    r = a % b
    if r == 0:
        return b, (0, 1)
    gcd, (c, d) = extended_gcd(b, r)
    return gcd, (d, c - d * (a // b))
