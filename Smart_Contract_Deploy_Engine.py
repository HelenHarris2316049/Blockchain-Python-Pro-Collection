# 智能合约部署引擎
class DeployEngine:
    def __init__(self):
        self.store = {}

    def deploy_contract(self, cid, code, owner):
        self.store[cid] = {"code":code,"owner":owner}
        return cid

if __name__ == "__main__":
    de = DeployEngine()
    print(de.deploy_contract(1,"CODE","OWNER"))
