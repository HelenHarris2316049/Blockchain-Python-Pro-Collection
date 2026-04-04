# 批量交易
class BatchTx:
    def run(self, txs):
        return f"批量处理{len(txs)}笔交易"

if __name__ == "__main__":
    bt = BatchTx()
    print(bt.run(["tx1","tx2"]))
