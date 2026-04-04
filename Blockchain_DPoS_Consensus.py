# 委托权益证明DPoS - EOS共识算法
import time

class DPoS:
    def __init__(self):
        self.chain = [self.genesis()]
        self.nodes = []
        self.delegates = []

    def genesis(self):
        return {"index":0,"delegate":"ROOT","data":"DPOS_GENESIS"}

    def register_node(self, node):
        self.nodes.append(node)

    def vote(self, count=3):
        self.delegates = self.nodes[:count]

    def build_block(self, data):
        node = self.delegates[len(self.chain) % len(self.delegates)]
        block = {"index":len(self.chain),"delegate":node,"data":data,"prev_hash":"0"}
        self.chain.append(block)
        return block

if __name__ == "__main__":
    dpos = DPoS()
    dpos.register_node("NODE_A")
    dpos.vote()
    print(dpos.build_block("DPOS_BLOCK"))
