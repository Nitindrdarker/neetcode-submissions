class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            a, b, v = equations[i][0], equations[i][1], values[i]
            adj[a].append((b, v))
            adj[b].append((a, 1/v))
    
        visited = set()

        def util(node, target):
            if node not in adj:
                return -1
            if node in visited:
                return -1
            if node == target:
                return 1
            
            visited.add(node)
            for neigh, value in adj[node]:
                v = util(neigh, target) * value
                if v >= 0:
                    visited.remove(node)
                    return v
            visited.remove(node)
            return -1
        res = []
        for a, b in queries:
            res.append(util(a, b))
        return res
                
            