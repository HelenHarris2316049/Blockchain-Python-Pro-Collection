# 借贷协议
class Lend:
    def loan(self, collateral, amount):
        return collateral>amount

if __name__ == "__main__":
    l = Lend()
    print(l.loan(200,100))
