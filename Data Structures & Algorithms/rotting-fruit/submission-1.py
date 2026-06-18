class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        row = len(grid)
        col = len(grid[0])
        freshCount = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    freshCount += 1

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        while q:
            i, j, t = q.popleft()
            res = max(t, res)
            for r, c in neighbors:
                nr, nc = i + r, j + c
                if nr >= row or nc >= col or nr < 0 or nc < 0:
                    continue
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    freshCount -= 1
                    q.append((nr, nc, t+1))
            
        return res if freshCount == 0 else -1
    [2,1,1]
    [0,1,1]
    [1,0,1]

            