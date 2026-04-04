# 区块链浏览器核心
class Explorer:
    def __init__(self, chain):
        self.chain = chain

    def get_block(self, idx):
        return self.chain[idx] if idx<len(self.chain) else None

if __name__ == "__main__":
    e = Explorer([1,2,3])
    print(e.get_block(0))
