class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        nodes = set()
        for word in words:
            for char in word:
                nodes.add(char)
        for i in range(1, len(words)):
            b = words[i]
            a = words[i-1]
            i = 0
            j = 0
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1
            
            if i >= len(a) or j >= len(b):
                if j == len(b) and i < len(a):
                    return ""
                continue
            if a[i] not in adj:
                adj[a[i]] = []
            adj[a[i]].append(b[j])
            
        
        stack = []
        visited = set()
        done = set()
        
        def topo(node):
            if node in done:
                return True
            if node in visited:
                return False
            visited.add(node)
            for neigh in adj.get(node, []):
                if topo(neigh) == False:
                    return False
            visited.remove(node)
            done.add(node)
            stack.append(node)
            return True
       
        for c in nodes:
            if not topo(c):
                return ''

        return ''.join(stack[::-1])
            
            
        


        


