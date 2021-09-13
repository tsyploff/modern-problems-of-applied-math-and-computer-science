
class Vigenere:

    def __init__(self, key: str = ""):
        self.key = key

    def set_key(self, key: str) -> None:
        if len(key) >= 1:
            self.key = key
        else:
            raise ValueError("Key word must be non-empty")

    def encrypt(self, message: str) -> str:
        n: int = len(self.key)
        return "".join([chr(ord(message[i]) + ord(self.key[i % n])) for i in range(len(message))])

    def decrypt(self, message: str) -> str:
        n: int = len(self.key)
        return "".join([chr(ord(message[i]) - ord(self.key[i % n])) for i in range(len(message))])
