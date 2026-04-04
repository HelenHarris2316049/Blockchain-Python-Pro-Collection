# Gas费计算
class Gas:
    def calc(self, size):
        return size*10

if __name__ == "__main__":
    g = Gas()
    print(g.calc(100))
