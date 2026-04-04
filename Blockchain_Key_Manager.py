# 密钥管理
class KeyMgr:
    def __init__(self):
        self.keys = {}

    def save(self, user, key):
        self.keys[user] = key

if __name__ == "__main__":
    km = KeyMgr()
    km.save("USER","KEY")
