# 风险预警
class Risk:
    def check(self, tx):
        return "高风险" if tx["value"]>1000 else "安全"

if __name__ == "__main__":
    r = Risk()
    print(r.check({"value":5000}))
