# 轻节点
class LightNode:
    def __init__(self):
        self.headers = []

    def add_header(self, h):
        self.headers.append(h)

if __name__ == "__main__":
    ln = LightNode()
    ln.add_header("HASH")
