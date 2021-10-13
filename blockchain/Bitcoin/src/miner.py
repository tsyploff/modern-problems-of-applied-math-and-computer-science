from hashlib import md5
from typing import List, Tuple

from .block import Block
from .client import Client
from .transaction import Transaction


class Miner(Client):
    def verify(self, transaction: Transaction):
        return self.check_signature(transaction.id, transaction.signature)

    def create_block(
        self, chain: List[Block], transactions: List[Transaction]
    ) -> Block:
        last_block = chain[-1]
        block = Block(previous_block_hash=last_block.nonce, nonce=self.mine(last_block))
        for transaction in transactions:
            if self.verify(transaction):
                block.add_transaction(transaction)
            else:
                print("Incorrect transaction has been found!")
        return block

    def __str__(self):
        return "Miner" + str(self.name)

    @staticmethod
    def check_signature(message: int, signature: Tuple[int, Tuple[int, int]]) -> bool:
        s, (e, n) = signature
        return message == pow(s, e, n)

    @staticmethod
    def mine(block: Block, difficulty=1) -> str:
        prefix = "0" * difficulty
        for attempt in range(1000):
            digest = md5((str(hash(block)) + str(attempt)).encode()).hexdigest()
            if digest.startswith(prefix):
                return digest
