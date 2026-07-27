class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: set() for i in range(numCourses)}
        child = {}
        for a, b in prerequisites:
            adj[b].add(a)
    
        def util(node):
            if len(adj[node]) == 0:
                return set()
            if node in child:
                return child[node]
            for neigh in adj[node]:
                
                subSet = util(neigh)
                if node not in child:
                    child[node] = set()
                child[node].add(neigh)
                for ele in subSet:
                    child[node].add(ele)
            return child[node]

        for i in range(numCourses):
            util(i)
        res = []
        for u, v in queries:
            res.append(v in child and u in child[v])
        return res


        


        

        