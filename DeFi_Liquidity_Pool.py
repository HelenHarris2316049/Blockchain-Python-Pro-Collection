# DeFi流动池
class LPool:
    def __init__(self):
        self.pool = {"A":0,"B":0}

    def add(self, a, b):
        self.pool["A"]+=a
        self.pool["B"]+=b

if __name__ == "__main__":
    lp = LPool()
    lp.add(100,200)
