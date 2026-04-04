# 跨链中继协议
class CrossChain:
    def relay(self, from_chain, to_chain, data):
        return f"从{from_chain}中继到{to_chain}：{data}"

if __name__ == "__main__":
    cc = CrossChain()
    print(cc.relay("ETH","BSC","DATA"))
