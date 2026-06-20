class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [0 for i in range(n)]
    def union(self, a, b) -> bool:
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return True
        else:
            if self.size[ap] < self.size[bp]:
                self.parent[ap] = bp
                self.size[bp] += self.size[ap]
            else:
                self.parent[bp] = ap
                self.size[ap] += self.size[bp]
        return False
    def find(self, a):
        while a != self.parent[a]:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        uf = UnionFind(len(edges) + 1)
        for i, j in edges:
            if uf.union(i, j):
                return [i, j]
        

    