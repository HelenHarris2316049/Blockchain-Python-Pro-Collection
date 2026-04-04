# P2P去中心化网络 - 节点通信
import socket
import threading

class P2P:
    def __init__(self, port):
        self.port = port
        self.peers = []

    def run(self):
        s = socket.socket()
        s.bind(("0.0.0.0", self.port))
        s.listen(3)
        while True:
            c, addr = s.accept()
            self.peers.append(addr)
            c.close()

    def connect(self, ip, p):
        self.peers.append((ip,p))

if __name__ == "__main__":
    node = P2P(9999)
    threading.Thread(target=node.run, daemon=True).start()
    print("P2P节点启动")
