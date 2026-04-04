# Layer2分片扩容
class Sharding:
    def __init__(self, count=4):
        self.shards = [[]for _ in range(count)]

    def add(self, data):
        idx = hash(data)%len(self.shards)
        self.shards[idx].append(data)

if __name__ == "__main__":
    s = Sharding()
    s.add("TX")
    print(s.shards)
