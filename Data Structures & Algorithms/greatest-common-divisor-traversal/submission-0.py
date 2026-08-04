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
            self.size[bp] += self.size[ap]
            self.parent[ap] = bp
        else:
            self.size[ap] += self.size[bp]
            self.parent[bp] = ap
        return 
        



class Solution:
    def primeFactor(self, num):
        i = 2
        factors = set()
        while num % 2 == 0:
            factors.add(i)
            num = num // 2
            
        i += 1
        while i * i <= num:
            if num % i == 0:
                num = num // i
                factors.add(i)
                continue
            i = i + 2
        if num > 1:
            factors.add(num)
        return factors
            
            


    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        adj = defaultdict(list)
        visited = set()
        uf = UnionFind(len(nums))
        for idx, num in enumerate(nums):
            factors = self.primeFactor(num)
            for factor in factors:
                adj[factor].append(idx)
        
        for factor in adj:
            l = adj[factor]
            a = l[0]
            for i in range(1, len(l)):
                uf.union(a, l[i])
        
        root = uf.find(0)
        for i in range(1, len(nums)):
            parent = uf.find(i)
            if parent != root:
                return False
        return True

                
        

        
