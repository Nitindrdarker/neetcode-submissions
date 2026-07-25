class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def util(i, j):
            if i >= row or j >= col or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if grid[i][j] == -1:
                return 0
            grid[i][j] = -1
            left = util(i, j-1)
            right = util(i, j+1)
            up = util(i-1, j)
            down = util(i+1, j)
            return left + right + up + down
        v = 0
        for i in range(row):
            for j in range(col):
                v = max(v, util(i, j))
        return v
        
