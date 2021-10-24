import datetime as dt
from typing import List, Optional, Tuple, Union
from .client import Client


class Transaction:
    identificators: List[int] = [2 ** 16]

    def __init__(
        self, sender: Union[Client, str], recipient: Client, value: Union[int, float]
    ):
        # sender либо клиент, либо 'Server' (если это первая транзакция в цепи)
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = dt.datetime.now()
        self.id = Transaction.identificators[-1] + 1
        self.signature: Optional[Tuple[int, Tuple[int, int]]] = sender.sign(
            self.id
        ) if sender != "Server" else None
        Transaction.identificators.append(self.id)

    def __str__(self):
        return f"Transaction(sender={self.sender}, recipient={self.recipient}, value={self.value}, time={self.time})"
