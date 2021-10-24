from typing import List, Optional
from .transaction import Transaction


class Block:
    identificators: List[int] = [0]

    def __init__(self, previous_block_hash: Optional[str] = None, nonce: str = ""):
        self.verified_transactions: List[Transaction] = []
        self.previous_block_hash = previous_block_hash
        self.nonce = nonce
        self.id = Block.identificators[-1] + 1
        Block.identificators.append(self.id)

    def __str__(self):
        return f"Block(id={self.id}, previous_block_hash={self.previous_block_hash}, nonce={self.nonce})"

    def add_transaction(self, transaction: Transaction):
        self.verified_transactions.append(transaction)

    def set_nonce(self, nonce: str):
        self.nonce = nonce
