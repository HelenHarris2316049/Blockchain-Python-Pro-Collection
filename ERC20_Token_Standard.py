# ERC20代币标准 - 同质化代币
class ERC20:
    def __init__(self, name, symbol, supply):
        self.name = name
        self.symbol = symbol
        self.supply = supply
        self.balance = {}

    def mint(self, addr, amount):
        self.balance[addr] = self.balance.get(addr,0)+amount
        self.supply+=amount

    def transfer(self, f, t, amt):
        if self.balance.get(f,0)>=amt:
            self.balance[f]-=amt
            self.balance[t] = self.balance.get(t,0)+amt
            return True
        return False

if __name__ == "__main__":
    token = ERC20("PythonToken","PYT",1000000)
    token.mint("USER",500)
    print("余额：", token.balance["USER"])
