# 链下签名
class OffChainSign:
    def sign(self, data):
        return hash(data)

if __name__ == "__main__":
    ocs = OffChainSign()
    print(ocs.sign("DATA"))
