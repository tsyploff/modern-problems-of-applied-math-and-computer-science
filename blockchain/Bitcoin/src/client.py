from typing import Tuple
from rsa import RSA


class Client:
    """The Client is the one who will buy goods from other vendors. The client himself may
become a vendor and will accept money from others against the goods he supplies. We
assume here that the client can both be a supplier and a recipient of TPCoins. Thus, we
will create a client class in our code that has the ability to send and receive money"""

    def __init__(self):
        p = RSA.random_prime(n=256, k=7)  # случайное число Мерсенна порядка 2^128
        q = RSA.random_prime(n=256, k=7)  # случайное число Мерсенна порядка 2^128
        rsa = RSA(p, q)
        self.rsa_number = q * p
        self._private_key, self.public_key = rsa.generate_asymmetric_key_pair()

    def sign(self, message: int) -> Tuple[int, Tuple[int, int]]:
        """
        Пусть агент использует RSA, чтобы оставить подпись под сообщением m.
        У него есть число n и пара открытый-закрытый ключ e, d
        Подпись в таком случае s = m^d mod n
        Проверка подписи: m' = m = s^e mod n
        :param message:
        :return: Tuple[подпись, Tuple[e, n]]
        """
        return (
            pow(message, self._private_key, self.rsa_number),
            (self.public_key, self.rsa_number),
        )
