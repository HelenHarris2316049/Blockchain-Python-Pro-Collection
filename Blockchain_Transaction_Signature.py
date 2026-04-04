# 交易数字签名 - 防篡改
import hashlib
import ecdsa
import binascii

class SignTx:
    def __init__(self):
        self.private = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.public = self.private.get_verifying_key()

    def sign(self, tx):
        h = hashlib.sha256(str(tx).encode()).digest()
        return binascii.hexlify(self.private.sign(h)).decode()

    def check(self, tx, sig):
        h = hashlib.sha256(str(tx).encode()).digest()
        return self.public.verify(binascii.unhexlify(sig), h)

if __name__ == "__main__":
    s = SignTx()
    tx = {"from":"A","to":"B","value":10}
    sig = s.sign(tx)
    print("验证结果：", s.check(tx, sig))
