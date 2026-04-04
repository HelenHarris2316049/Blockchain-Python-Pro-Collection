# NFT市场
class NFTMarket:
    def __init__(self):
        self.orders = {}

    def list_nft(self, tid, price):
        self.orders[tid] = price

if __name__ == "__main__":
    m = NFTMarket()
    m.list_nft(1,100)
