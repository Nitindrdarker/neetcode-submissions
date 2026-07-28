class UF:
    def __init__(self):
        self.parent = {}
        self.size = {}

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
         
    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a
    def create(self, email):
        self.parent[email] = email
        self.size[email] = 0


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF()
        name_email = {}
        res = {}
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                
                uf.create(account[i])
                name_email[account[i]] = name

        for account in accounts:
            for i in range(2, len(account)):
                uf.union(account[1], account[i])
                
        for i in name_email:
            parent = uf.find(i)
            if parent not in res:
                res[parent] = []
            res[parent].append(i)
        ans = []
        for email in name_email:
            if email in res:
                l = [name_email[email]] + sorted(res[email])
                ans.append(l)
        return ans
            


        
        
        

                

        

        
        


        