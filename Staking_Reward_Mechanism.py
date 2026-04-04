# 质押奖励机制
class StakeReward:
    def calc(self, amount, days):
        return amount*0.01*days

if __name__ == "__main__":
    sr = StakeReward()
    print(sr.calc(1000,30))
