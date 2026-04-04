# 同态加密 - 密文计算
class HE:
    def encrypt(self, x):
        return x*100

    def add(self, a, b):
        return a+b

    def decrypt(self, x):
        return x//100

if __name__ == "__main__":
    he = HE()
    a = he.encrypt(5)
    b = he.encrypt(3)
    print(he.decrypt(he.add(a,b)))
