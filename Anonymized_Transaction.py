# 匿名交易
class AnonyTx:
    def hide(self, addr):
        return f"ANON_{hash(addr)%10000}"

if __name__ == "__main__":
    a = AnonyTx()
    print(a.hide("ADDR"))
