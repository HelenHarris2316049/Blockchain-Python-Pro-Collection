# 奖励分发
class RewardDistribute:
    def send(self, list, total):
        return total/len(list)

if __name__ == "__main__":
    rd = RewardDistribute()
    print(rd.send(["A","B"],100))
