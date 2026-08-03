class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        adj1 = {i+1: [] for i in range(k)}
        adj2 = {i+1: [] for i in range(k)}

        for a, b in rowConditions:
            adj1[a].append(b)
        
        for a, b in colConditions:
            adj2[a].append(b)
        
        def util(node, visited, done, stack, adj):
            if node in visited:
                return False
            if node in done:
                return True
            visited.add(node)
            for neigh in adj[node]:
                if not util(neigh, visited, done, stack, adj):
                    return False
            visited.remove(node)
            stack.append(node)
            done.add(node)
            return True

        stack1 = []
        stack2 = []
        visited = set()
        done = set()
        for i in range(1, k+1):
            if not util(i, visited, done, stack1, adj1):
                return []
        visited = set()
        done = set()
        for i in range(1, k+1):
            if not util(i, visited, done, stack2, adj2):
                return []
        s1Index = {}
        s2Index = {}
        for i, val in enumerate(stack1):
            s1Index[val] = ((k - 1) - i)
        for i, val in enumerate(stack2):
            s2Index[val] = ((k - 1) - i)

        res = [[0 for i in range(k)] for j in range(k)]
        for i in range(1, k +1):
            row = s1Index[i]
            col = s2Index[i]
            res[row][col] = i
        return res

        
            


        

