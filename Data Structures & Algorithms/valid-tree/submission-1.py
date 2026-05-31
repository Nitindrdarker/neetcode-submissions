class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        visited = set()
        completed = set()
        for f, t in edges:
            adj[f].append(t)
            adj[t].append(f)

        def util(node):
            if node in completed:
                return False
            if node in visited:
                return True
            visited.add(node)
            for neigh in adj[node]:
                if neigh == node:
                    return False
                if util(neigh) == False:
                    return False
            visited.remove(node)
            completed.add(node)
            return True
        util(0)
        return len(completed) == n

        
        