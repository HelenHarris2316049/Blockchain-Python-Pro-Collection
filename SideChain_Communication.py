# 侧链通信
class SideChain:
    def send(self, main, side, data):
        return f"主链{main}→侧链{side}：{data}"

if __name__ == "__main__":
    sc = SideChain()
    print(sc.send("MAIN","SIDE","TEST"))
