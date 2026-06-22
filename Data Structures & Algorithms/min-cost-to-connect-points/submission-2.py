class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        minHeap = []
        adj = {}
        for i in range(len(points)):
            y1, x1 = points[i]
            for j in range(i+1, len(points)):
                y2, x2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                if i not in adj:
                    adj[i] = []
                if j not in adj:
                    adj[j] = []
                adj[i].append((dist, j))
                adj[j].append((dist, i))
                

        visited = {}
        res = 0
        heapq.heappush(minHeap, (0, 0)) #d, to
        while minHeap:
            d, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            if i not in visited or visited[i] > d:
                visited[i] = d
            else:
                continue

            for dist, to in adj[i]:
                if to not in visited:
                    heapq.heappush(minHeap, (dist, to)) 
    
        return sum(visited.values())

            



            