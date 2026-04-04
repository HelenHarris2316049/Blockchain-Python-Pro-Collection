# 区块链API网关
class APIGateway:
    def request(self, path):
        return f"API/{path}"

if __name__ == "__main__":
    api = APIGateway()
    print(api.request("block"))
