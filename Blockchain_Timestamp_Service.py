# 链上时间戳服务
import time
class Timestamp:
    def get(self):
        return time.time()

if __name__ == "__main__":
    ts = Timestamp()
    print(ts.get())
