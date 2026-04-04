# 零知识证明核心
class ZKP:
    def prove(self, secret):
        return hash(secret)

    def verify(self, secret, proof):
        return hash(secret)==proof

if __name__ == "__main__":
    zkp = ZKP()
    p = zkp.prove("SECRET")
    print("验证：", zkp.verify("SECRET",p))
