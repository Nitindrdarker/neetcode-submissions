class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if (n < 2):
            return [i for i in range(n)]
        adj = {i:set() for i in range(n)}
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        q = collections.deque()
        for i in range(n):
            if len(adj[i]) == 1:
                q.append(i)
        res = []
        while len(adj) > 2:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                for neigh in adj[node]:
                    adj[neigh].remove(node)
                    if len(adj[neigh]) == 1:
                        q.append(neigh)
                del adj[node]
        return list(adj.keys())

        