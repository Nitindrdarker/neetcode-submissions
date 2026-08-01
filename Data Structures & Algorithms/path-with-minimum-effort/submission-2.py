class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q = []
        q.append((0, 0, 0)) #diff, i, j
        row = len(heights)
        col = len(heights[0])
        visited = set()
        res = float("inf")
        while q:
            diff, i, j = heapq.heappop(q)
            if i == row - 1 and j == col - 1:
                res = min(res, diff)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for r, c in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nr, nc = r + i, c + j
                if nr >= row or nr < 0 or nc >= col or nc < 0 or (nr, nc) in visited:
                    continue
                heapq.heappush(q, (max(diff, abs(heights[i][j] - heights[nr][nc])), nr, nc))
        return res


    
        
            
                



        