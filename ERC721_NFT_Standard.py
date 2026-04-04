# ERC721 NFT标准 - 非同质化代币
class NFT:
    def __init__(self):
        self.owner = {}
        self.uri = {}

    def mint(self, tid, addr, url):
        self.owner[tid] = addr
        self.uri[tid] = url

    def transfer(self, tid, f, t):
        if self.owner.get(tid)==f:
            self.owner[tid]=t
            return True
        return False

if __name__ == "__main__":
    nft = NFT()
    nft.mint(1,"CREATOR","ipfs://nft1")
    print("持有者：", nft.owner[1])
