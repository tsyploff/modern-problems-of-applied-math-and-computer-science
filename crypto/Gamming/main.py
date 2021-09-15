
from src import Gamming

if __name__ == '__main__':
    crypt: Gamming = Gamming()
    while True:
        key: str = input("Введите кодовое слово или 'stop', чтобы выйти:\n")
        if key.lower() == "stop":
            break

        crypt.set_key(key)

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
