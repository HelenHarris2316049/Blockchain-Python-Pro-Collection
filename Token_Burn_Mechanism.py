# 代币燃烧
class Burn:
    def __init__(self):
        self.total = 1000000

    def burn(self, amount):
        self.total -= amount

if __name__ == "__main__":
    b = Burn()
    b.burn(1000)
    print(b.total)
