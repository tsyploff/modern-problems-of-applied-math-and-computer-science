
from src import Caesar

if __name__ == '__main__':
    crypt: Caesar = Caesar()
    while True:
        key: str = input("Введите кодовое слово или 'stop', чтобы выйти:\n")
        if key.lower() == "stop":
            break

        crypt.set_key(int(key))

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
        elif use.lower() == "decrypt":
            for key, text in crypt.decrypt(message):
                print("Ключ {} приводит к сообщению '{}'".format(key, text))
        else:
            print(crypt.encrypt(message))
