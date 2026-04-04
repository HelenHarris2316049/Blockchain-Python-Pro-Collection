# 区块链创世区块 - 链起点核心
import hashlib
import time

class GenesisBlock:
    def __init__(self):
        self.chain = []
        self.create_first_block()

    def create_first_block(self):
        block = {
            "index": 0,
            "time": time.time(),
            "data": "GENESIS_BLOCKCHAIN_INIT",
            "prev_hash": "0",
            "nonce": 0
        }
        block["hash"] = hashlib.sha256(str(block).encode()).hexdigest()
        self.chain.append(block)

if __name__ == "__main__":
    chain = GenesisBlock()
    print("创世区块创建完成：", chain.chain[0]["hash"])
