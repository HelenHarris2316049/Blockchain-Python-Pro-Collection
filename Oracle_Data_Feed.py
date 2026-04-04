# 预言机数据喂价
class Oracle:
    def price(self):
        return 50000

if __name__ == "__main__":
    o = Oracle()
    print(o.price())
