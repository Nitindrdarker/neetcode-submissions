class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        completed = set()

        adj = {i:[] for i in range(numCourses)}
        for f, n in prerequisites:
            adj[f].append(n)
        visited = set()
        stack = []
        

        def util(node):
            if node in completed:
                return True
            if node in visited:
                return False
            visited.add(node)
            for neigh in adj[node]:
                if util(neigh) == False:
                    return False
            visited.remove(node)
            completed.add(node)
            stack.append(node)
        
        
        for i in range(numCourses):
            
            if util(i) == False:
                return []
            
        
        return stack
            
            