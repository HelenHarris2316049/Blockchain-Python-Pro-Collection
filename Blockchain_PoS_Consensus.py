# 权益证明PoS - 以太坊共识算法
import random
import time

class PoSChain:
    def __init__(self):
        self.chain = [self.genesis()]
        self.stake = {}

    def genesis(self):
        return {"index":0,"validator":"GENESIS","data":"POS_INIT","prev_hash":"0"}

    def add_stake(self, addr, amount):
        self.stake[addr] = amount

    def choose_validator(self):
        total = sum(self.stake.values())
        pick = random.uniform(0, total)
        current = 0
        for k, v in self.stake.items():
            current += v
            if current >= pick:
                return k

    def add_block(self, data):
        val = self.choose_validator()
        block = {"index":len(self.chain),"validator":val,"data":data,"prev_hash":self.chain[-1]["prev_hash"]}
        self.chain.append(block)
        return block

if __name__ == "__main__":
    pos = PoSChain()
    pos.add_stake("ADDR1", 100)
    print("区块生成：", pos.add_block("PoS_DATA"))
