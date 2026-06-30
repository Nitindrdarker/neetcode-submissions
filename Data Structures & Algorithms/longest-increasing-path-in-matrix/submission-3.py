class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        memo = {}
        def util(i, j):
            if i >= row or j >= col or i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            top = down = left = right = 0
            if i + 1 < row and grid[i+1][j] > grid[i][j]:
                down = util(i+1, j)
            if i - 1 >= 0 and grid[i-1][j] > grid[i][j]:
                top = util(i-1, j)
            if j - 1 >= 0 and grid[i][j-1] > grid[i][j]:
                left = util(i, j-1)
            if j + 1 < col and grid[i][j+1] > grid[i][j]:
                right = util(i, j+1)
            memo[(i, j)] = max(top, down, left, right) + 1
            return memo[(i, j)]
        res = 0
        
        for i in range(row):
            for j in range(col):
                val = util(i, j)
                res = max(res, val)

        return res

