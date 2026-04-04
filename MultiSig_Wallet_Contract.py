# 多签钱包合约
class MultiSig:
    def __init__(self, owners, required):
        self.owners = owners
        self.required = required
        self.signs = {}

    def sign(self, owner, tx):
        self.signs[tx] = self.signs.get(tx,0)+1

    def exec(self, tx):
        return self.signs.get(tx,0)>=self.required

if __name__ == "__main__":
    ms = MultiSig(["A","B"],2)
    ms.sign("A","TX1")
    print(ms.exec("TX1"))
