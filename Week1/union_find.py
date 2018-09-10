import sys


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


class QuickUnion:
    def __init__(self, N):
        self.id = list(range(N))

    def union(self, p, q):
        self.id[self.root(q)] = self.root(p)
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

class WeightedQUAndCompr:
    def __init__(self, N):
        self.id = list(range(N))
        self.sz = [1]*N
        
    # lg_2^N        
    def union(self, p, q):
        p_rt = self.find(p)
        q_rt = self.find(q)
        if (p_rt == q_rt):
            return
        if self.sz[p_rt] < self.sz[q_rt]:
            self.id[p_rt] = q_rt
            self.sz[q_rt] += self.sz[p_rt]
        else:
            self.id[q_rt] = p_rt
            self.sz[p_rt] += self.sz[q_rt]

    def find(self, i):
        if i != self.id[i]:
            self.id[i] = self.find(self.id[i])
        return self.id[i]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return -1
    
def parse_UF():
    f_name = sys.argv[1]

    with open(f_name) as f:
        N = int(f.readline())
        # uf = QuickFind(N)
        # uf = QuickUnion(N)
        uf = WeightedQUAndCompr(N)
        for line in f:
            p, q = list(map(int, line.split()))
            if not uf.connected(p,q):
                uf.union(p,q)
                # print("Connecting ",p,q)
                print(uf.id)
        
        # executing find(i) will compress the path
        uf.connected(p,q)
        print(uf.id, uf.sz)

        
if __name__ == "__main__":
    parse_UF()
