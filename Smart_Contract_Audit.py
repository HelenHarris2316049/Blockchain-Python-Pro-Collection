# 智能合约审计
class Audit:
    def check(self, code):
        return "安全" if "safe" in code else "风险"

if __name__ == "__main__":
    a = Audit()
    print(a.check("safe_code"))
