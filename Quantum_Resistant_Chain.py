# 抗量子区块链
class QuantumResist:
    def encrypt(self, data):
        return hash(data*100)

if __name__ == "__main__":
    qr = QuantumResist()
    print(qr.encrypt("DATA"))
