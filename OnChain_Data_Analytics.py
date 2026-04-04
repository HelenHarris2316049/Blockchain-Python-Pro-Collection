# 链上数据分析
class Analytics:
    def count(self, chain):
        return len(chain)

if __name__ == "__main__":
    a = Analytics()
    print(a.count([1,2,3]))
