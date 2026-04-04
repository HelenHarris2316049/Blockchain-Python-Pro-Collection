# IPFS文件上链
class IPFS:
    def upload(self, file):
        return f"IPFS_HASH_{hash(file)}"

if __name__ == "__main__":
    ipfs = IPFS()
    print(ipfs.upload("test.txt"))
