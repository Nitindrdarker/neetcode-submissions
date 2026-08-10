class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        row = len(grid)
        col = len(grid[0])
        visited = set()
        while heap:
            s, i, j = heapq.heappop(heap)
            if i == row - 1 and j == col - 1:
                return s
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for r, c in ([1, 0], [0, 1]):
                nr, nc = r + i, c + j
                if nr < row and nc < col and (nr, nc) not in visited:
                    heapq.heappush(heap, (s + grid[nr][nc], nr, nc))
        return -1
            

        