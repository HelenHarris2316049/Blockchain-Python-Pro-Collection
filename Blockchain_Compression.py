# 区块数据压缩
class Compress:
    def zip(self, data):
        return data*2

if __name__ == "__main__":
    c = Compress()
    print(c.zip("BLOCK"))
