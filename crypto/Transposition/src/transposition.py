
from typing import List


class Transposition:

    def __init__(self, width: int = 5):
        self.width = width  # ширина таблицы

    def get_width(self) -> int:
        return self.width

    def set_width(self, width: int):
        self.width = width

    def encrypt(self, message: str, width: int = None) -> str:
        """
        Используется для шифрования и дешифрования
        :param message: сообщение
        :param width: ширина таблицы
        :return: преобразованное сообщение
        """
        size = self.width if (width is None) else width
        length = len(message)  # длина сообщения

        if length % size == 0:
            full_length = length
        else:
            full_length = (1 + length // size) * size  # длина расширенного сообщения

        reminder = full_length - length  # разница длин расширенного и исходного сообщений
        to_encrypt = message + "&" * reminder  # расширенное сообщение
        table = [list(to_encrypt[i:i + size]) for i in range(0, full_length, size)]  # таблица
        transposed = Transposition.transpose(table)  # транспонированная таблица
        return "".join("".join(row) for row in transposed)

    @staticmethod
    def transpose(table: List[List[str]]) -> List[List[str]]:
        n = len(table)
        m = len(table[0])
        return [[table[i][j] for i in range(n)] for j in range(m)]
