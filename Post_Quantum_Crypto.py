# 后量子密码
class PQC:
    def sign(self, data):
        return hash(data+str(123))

if __name__ == "__main__":
    pqc = PQC()
    print(pqc.sign("MSG"))
