# 链上通知
class Notify:
    def send(self, msg):
        print(f"通知：{msg}")

if __name__ == "__main__":
    n = Notify()
    n.send("交易成功")
