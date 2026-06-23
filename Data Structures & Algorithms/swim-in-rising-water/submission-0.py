class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        row = len(grid)
        col = len(grid[0])

        neighbors = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        heapq.heappush(heap, (0, 0, 0)) #dist, i, j
        visited = {(0, 0)}
        res = 0
        while heap:
            d, i, j = heapq.heappop(heap)
            res = max(res, grid[i][j])
            if i == row - 1 and j == col - 1:
                return res
            visited.add((i, j))
            for r, c in neighbors:
                nr, nc = r + i, c + j
                if nr >= row or nr < 0 or nc >= col or nc < 0:
                    continue
                if (nr, nc) in visited:
                    continue
                heapq.heappush(heap, (grid[nr][nc], nr, nc))
        return res
                
                



