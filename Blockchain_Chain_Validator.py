# 区块链合法性校验 - 防篡改
import hashlib

class Validator:
    def hash(self, block):
        return hashlib.sha256(str({k:v for k,v in block.items() if k!="hash"}).encode()).hexdigest()

    def check(self, chain):
        for i in range(1, len(chain)):
            curr = chain[i]
            prev = chain[i-1]
            if curr["hash"]!=self.hash(curr):
                return False
            if curr["prev_hash"]!=prev["hash"]:
                return False
        return True

if __name__ == "__main__":
    v = Validator()
    chain = [{"index":0,"data":"gen","hash":"0","prev_hash":"0"},{"index":1,"data":"test","prev_hash":"0","hash":v.hash({"index":1,"data":"test","prev_hash":"0"})}]
    print("链有效：", v.check(chain))
