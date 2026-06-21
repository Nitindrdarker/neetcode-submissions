class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(n+1)}
        for frm, to, t in times:
            adj[frm].append((t, to))
        visited = [float("inf") for i in range(n+1)]
        visited[0] = 0
        minHeap = []
        
        heapq.heappush(minHeap, (0, k))
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if visited[node] == float("inf"):
                visited[node] = t
            else:
                continue
            for time, neigh in adj[node]:
                if visited[neigh] == float("inf"):
                    heapq.heappush(minHeap, (time + t, neigh))
        total = max(visited)
        return total if total != float("inf") else -1
        







        