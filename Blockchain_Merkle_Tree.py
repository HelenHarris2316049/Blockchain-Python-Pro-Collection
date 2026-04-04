# 默克尔树 - 交易快速校验
import hashlib

class Merkle:
    def __init__(self, txs):
        self.txs = [hashlib.sha256(str(x).encode()).hexdigest() for x in txs]

    def root(self):
        if len(self.txs)==1:
            return self.txs[0]
        new = []
        for i in range(0, len(self.txs), 2):
            l = self.txs[i]
            r = self.txs[i+1] if i+1<len(self.txs) else l
            new.append(hashlib.sha256((l+r).encode()).hexdigest())
        self.txs = new
        return self.root()

if __name__ == "__main__":
    m = Merkle(["tx1","tx2","tx3"])
    print("默克尔根：", m.root())
