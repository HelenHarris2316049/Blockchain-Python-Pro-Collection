# 白名单合约
class WhiteList:
    def __init__(self):
        self.wl = set()

    def add(self, addr):
        self.wl.add(addr)

    def check(self, addr):
        return addr in self.wl

if __name__ == "__main__":
    w = WhiteList()
    w.add("USER")
    print(w.check("USER"))
