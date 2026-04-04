# 椭圆曲线加密
import random

class ECC:
    def __init__(self):
        self.p = 23
        self.a = 1
        self.b = 1

    def gen_key(self):
        return random.randint(1,10)

if __name__ == "__main__":
    ecc = ECC()
    print("私钥：", ecc.gen_key())
