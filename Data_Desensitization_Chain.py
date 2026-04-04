# 链上数据脱敏
class Desensitize:
    def mask(self, data):
        return data[:2]+"****"+data[-2:]

if __name__ == "__main__":
    d = Desensitize()
    print(d.mask("12345678"))
