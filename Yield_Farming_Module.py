# 收益耕作
class YieldFarm:
    def earn(self, stake):
        return stake*0.02

if __name__ == "__main__":
    yf = YieldFarm()
    print(yf.earn(1000))
