# 软分叉升级
class SoftFork:
    def upgrade(self):
        return "协议升级完成"

if __name__ == "__main__":
    sf = SoftFork()
    print(sf.upgrade())
