# 轻量级智能合约虚拟机
class SVM:
    def __init__(self):
        self.contracts = {}

    def deploy(self, name, code):
        self.contracts[name] = code

    def run(self, name, data):
        if name in self.contracts:
            return f"执行{name}：{data}"
        return "合约不存在"

if __name__ == "__main__":
    vm = SVM()
    vm.deploy("Test","transfer")
    print(vm.run("Test","100"))
