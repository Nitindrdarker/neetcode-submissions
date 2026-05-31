class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [0 for i in range(n)]
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return 
        if self.size[ap] > self.size[bp]:
            self.size[ap] += self.size[bp]
            self.parent[bp] = ap
        else:
            self.size[bp] += self.size[ap]
            self.parent[ap] = bp
        return
        



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        s = set()
        for i in range(n):
            s.add(uf.find(i))
        return len(s)
