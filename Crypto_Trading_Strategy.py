# 加密货币量化策略
class Strategy:
    def trade(self, price):
        return "买入" if price<100 else "卖出"

if __name__ == "__main__":
    s = Strategy()
    print(s.trade(90))
