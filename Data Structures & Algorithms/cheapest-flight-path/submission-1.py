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
        while heap:
            price, step, node = heapq.heappop(heap)
            if node == dst:
                return price
            if step >= k:
                continue
            if node not in adj:
                continue
            for p, neigh in adj[node]:
                heapq.heappush(heap, (price + p, step + 1, neigh))
        return -1
            
                