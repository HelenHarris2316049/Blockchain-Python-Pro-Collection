# 防双花攻击
class AntiDoubleSpend:
    def __init__(self):
        self.spent = set()

    def check(self, txid):
        if txid in self.spent:
            return False
        self.spent.add(txid)
        return True

if __name__ == "__main__":
    ads = AntiDoubleSpend()
    print(ads.check("TX1"))
