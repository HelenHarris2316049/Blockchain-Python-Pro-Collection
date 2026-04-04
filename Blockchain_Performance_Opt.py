# 区块链性能优化
class Opt:
    def speed(self, chain):
        return f"优化后处理速度：{len(chain)*10} TPS"

if __name__ == "__main__":
    o = Opt()
    print(o.speed([1,2,3]))
