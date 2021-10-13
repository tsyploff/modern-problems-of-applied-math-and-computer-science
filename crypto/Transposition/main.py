
from src import Transposition

if __name__ == '__main__':
    crypt: Transposition = Transposition()
    while True:
        width: str = input("Введите ширину таблицы или 'stop', чтобы выйти:\n")
        if width.lower() == "stop":
            break

        crypt.set_width(int(width))

        message: str = input("Введите сообщение или 'stop', чтобы выйти:\n")
        if message.lower() == "stop":
            break

        print(
            "Нажмите enter, чтобы зашифровать сообщение;",
            "Введите 'decrypt', чтобы дешифровать сообщение;",
            "Введите 'stop', чтобы выйти."
        )
        use: str = input()
        if use.lower() == "stop":
            break
        else:
            print(crypt.encrypt(message))
