
from typing import Dict


class Caesar:

    def __init__(self, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", key: int = 0):
        self.alphabet = alphabet
        self.key = key
        self.hash_table: dict = {" ": " "}

    def set_hash_table(self) -> None:
        n = len(self.alphabet)
        self.hash_table = {self.alphabet[i]: self.alphabet[(i + self.key) % n] for i in range(n)}
        self.hash_table[" "] = " "

    def set_alphabet(self, alphabet: str) -> None:
        self.alphabet = alphabet
        self.set_hash_table()

    def set_key(self, key: int) -> None:
        self.key = key
        self.set_hash_table()

    def get_alphabet(self) -> str:
        return self.alphabet

    def get_key(self) -> int:
        return self.key

    def encrypt(self, message: str) -> str:
        if not all(symbol == " " or symbol in self.alphabet for symbol in message):
            raise ValueError("Символы сообщения не из алфавита")
        else:
            return "".join([self.hash_table[s] for s in message])

    def decrypt(self, message: str) -> Dict[int, str]:
        true_key = self.key

        result = {}
        for key in range(len(self.alphabet)):
            self.set_key(key)
            result[key] = self.encrypt(message)

        self.key = true_key
        return result
