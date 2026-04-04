# 区块同步
class Sync:
    def sync(self, local, remote):
        return remote[len(local):]

if __name__ == "__main__":
    s = Sync()
    print(s.sync([1,2],[1,2,3]))
