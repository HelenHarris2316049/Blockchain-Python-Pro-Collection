# 硬分叉升级
class HardFork:
    def upgrade(self, chain):
        return chain + ["FORK_BLOCK"]

if __name__ == "__main__":
    hf = HardFork()
    print(hf.upgrade([1,2]))
