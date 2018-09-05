import sys

class UnionFind:
    def __init__(self, N):
        self.id = list(range(N))

    def union(self, p, q):
        p_rt = rt(p)
        q_rt = rt(q)
        id[p_rt] = q_rt
    
    def connected(self, p, q):
        return root(p) == root(q)

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def count(self):
        return -1

class QuickUnion:
    def __init__(self, N):
        self.id = list(range(N))

    def union(self, p, q):
        id[p] = q
    
    def connected(self, p, q):
        return root(p) == root(q)

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i


class QuickFind:
    def __init__(self, N):
        self.id = list(range(N))

    def union(self, p, q):
        p_idx = self.id[p]
        q_idx = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == q_idx:
                self.id[i] = p_idx
    
    def connected(self, p, q):
        return self.id[p] == self.id[q]

    
def parse_UF():
    f_name = sys.argv[1]

    with open(f_name) as f:
        N = int(f.readline())
        uf = QuickFind(N);
        for line in f:
            p, q = list(map(int, line.split()))
            if not uf.connected(p,q):
                uf.union(p,q)
                # print("Connecting ",p,q)
                print(uf.id)
            
    
if __name__ == "__main__":
    parse_UF()
