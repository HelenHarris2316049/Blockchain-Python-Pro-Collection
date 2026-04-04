# 工作量证明PoW - 比特币共识算法
import hashlib
import time

class PoWChain:
    def __init__(self):
        self.chain = [self.genesis()]
        self.difficulty = 4

    def genesis(self):
        return {"index":0,"time":time.time(),"data":"GENESIS","prev_hash":"0","nonce":0,"hash":self.calc_hash({})}

    def calc_hash(self, block):
        return hashlib.sha256(str(block).encode()).hexdigest()

    def mine(self, data):
        prev = self.chain[-1]
        block = {"index":prev["index"]+1,"time":time.time(),"data":data,"prev_hash":prev["hash"],"nonce":0}
        while block["hash"][:self.difficulty] != "0"*self.difficulty:
            block["nonce"]+=1
            block["hash"]=self.calc_hash(block)
        self.chain.append(block)
        return block

if __name__ == "__main__":
    pow_chain = PoWChain()
    print("挖矿中...")
    block = pow_chain.mine("TEST_PoW")
    print("挖矿成功：", block["hash"])
