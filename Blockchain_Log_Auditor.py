# 日志审计
class LogAudit:
    def log(self, msg):
        print(f"AUDIT: {msg}")

if __name__ == "__main__":
    la = LogAudit()
    la.log("TX_SUCCESS")
