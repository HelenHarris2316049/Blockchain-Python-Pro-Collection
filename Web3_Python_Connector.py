# Web3连接
class Web3Connect:
    def connect(self, rpc):
        return f"连接{rpc}成功"

if __name__ == "__main__":
    w3 = Web3Connect()
    print(w3.connect("http://localhost:8545"))
