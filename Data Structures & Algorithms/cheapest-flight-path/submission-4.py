class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k = k+1
        q = collections.deque()
        adj = {}
        for f ,t, p in flights:
            if f not in adj:
                adj[f] = []
            adj[f].append((p, t))

        q.append((0, 0, src))
        visited = [float("inf") for i in range(n)]
        
        while q:
            price, step, node = q.popleft()
            if step >= k:
                continue
            if node not in adj:
                continue
            for p, neigh in adj[node]:
                if visited[neigh] > p + price:
                    visited[neigh] = p + price
                    q.append((price + p, step + 1, neigh))
        if visited[dst] != float("inf"):
            return visited[dst]
        return -1
            
                