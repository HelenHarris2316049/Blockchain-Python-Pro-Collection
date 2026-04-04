# 归档节点存储
class ArchiveNode:
    def __init__(self):
        self.history = []

    def save(self, data):
        self.history.append(data)

if __name__ == "__main__":
    an = ArchiveNode()
    an.save("BLOCK")
