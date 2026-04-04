# DAO治理核心
class DAO:
    def __init__(self):
        self.votes = {}

    def vote(self, prop, addr):
        self.votes[prop] = self.votes.get(prop,0)+1

if __name__ == "__main__":
    dao = DAO()
    dao.vote("PROP1","USER")
