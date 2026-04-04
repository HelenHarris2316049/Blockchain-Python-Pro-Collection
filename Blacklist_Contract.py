# 黑名单合约
class BlackList:
    def __init__(self):
        self.bl = set()

    def add(self, addr):
        self.bl.add(addr)

if __name__ == "__main__":
    b = BlackList()
    b.add("BAD")
