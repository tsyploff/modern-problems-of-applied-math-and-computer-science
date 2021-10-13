from random import choice
from typing import List


def __choose_next_prime(mask: List[bool]) -> int:
    """
    Возвращает первый индекс i списка mask: mask[i] == True.
    Если такого нет, возвращает -1
    """
    try:
        prime: int = mask.index(True)
        return prime
    except ValueError:
        return -1


def eratosthenes_sieve(n: int) -> List[int]:
    """
    Генерирует все простые числа p: p <= n
    """
    if n < 3:
        raise ValueError(f"Expected n >= 3, got {n}")

    mask: List[bool] = [False, False] + [True for _ in range(n - 1)]
    prime: int = 2
    primes: List[int] = []

    while prime != -1:
        primes.append(prime)
        for k in range(prime, n + 1, prime):
            mask[k] = False
        prime = __choose_next_prime(mask)

    return primes


def power_mod(n: int, k: int, p: int) -> int:
    """Вычисляет n^k mod p"""
    exponents = list(map(int, bin(k)[2:]))
    t = 1
    for m in exponents[:-1]:
        t = (t * n ** m) ** 2 % p
    return (t * n ** exponents[-1]) % p


def lucas_lehmer_primality_test(p: int) -> bool:
    """
    Проверяет, является ли простым число 2^p - 1.

    :param p: p - простое
    :return: является ли M_p простым
    """
    if p == 2:
        return True
    mersenne: int = 2 ** p - 1
    s: int = 4
    for i in range(1, p - 1):
        s = (s ** 2 - 2) % mersenne
    return s == 0


def mersenne_generator(n: int) -> List[int]:
    """
    Возвращает все числа Мерсенна, такие, что
    M_p = 2^p - 1, p <= n
    """
    primes: List[int] = list(filter(lucas_lehmer_primality_test, eratosthenes_sieve(n)))
    return [2 ** p - 1 for p in primes]


def prime_generator(n: int = 256, k: int = 10) -> int:
    """
    Возвращает простое число Мерсена, близкое к 2^n
    :param n: примерное количество бит в простом числе, обычно 256
    :param k: из скольки простых чисел будет выбираться случайное
    :return:
    """

    def distant_n(m: int) -> int:
        return abs(2 ** n - m)

    mersenne_primes: List[int] = sorted(mersenne_generator(2 * n), key=distant_n)
    return choice(mersenne_primes[: min(len(mersenne_primes), k)])
