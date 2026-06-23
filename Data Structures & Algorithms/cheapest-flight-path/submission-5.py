class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k = k+1
        heap = []
        adj = {}
        for f ,t, p in flights:
            if f not in adj:
                adj[f] = []
            adj[f].append((p, t))

        heapq.heappush(heap, (0, 0, src))
        visited = [float("inf") for i in range(n)]
        
        while heap:
            step, price, node = heapq.heappop(heap)
            
            if step > k:
                continue
            if visited[node] > price:
                visited[node] = price
            else:
                continue
            if node not in adj:
                continue
            
            for p, neigh in adj[node]:

                heapq.heappush(heap, (step + 1,price + p, neigh))
        if visited[dst] != float("inf"):
            return visited[dst]
        return -1
            
                