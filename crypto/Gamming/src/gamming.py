
class Gamming:

    def __init__(self, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ,.!?()", key: str = ""):
        self.alphabet = alphabet
        self.key = key

    def set_alphabet(self, alphabet: str) -> None:
        self.alphabet = alphabet

    def set_key(self, key: str) -> None:
        if not all(symbol == " " or symbol in self.alphabet for symbol in key):
            raise ValueError("Символы сообщения не из алфавита")
        else:
            self.key = key

    def get_alphabet(self) -> str:
        return self.alphabet

    def get_key(self) -> str:
        return self.key

    def encrypt(self, message: str) -> str:
        if not all(symbol == " " or symbol in self.alphabet for symbol in message):
            raise ValueError("Символы сообщения не из алфавита")
        else:
            result = []
            n = len(self.key)
            m = len(self.alphabet)
            for i in range(len(message)):
                if message[i] == " ":
                    result.append(" ")
                else:
                    s = self.alphabet.find(message[i])
                    k = self.alphabet.find(self.key[i % n])
                    result.append(self.alphabet[(s ^ k) % m])
            return "".join(result)
