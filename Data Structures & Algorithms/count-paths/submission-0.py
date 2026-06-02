class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = m
        col = n
        memo = [[0 for i in range(col)] for j in range(row)]
        def util(i, j):
            if i >= row or j >= col or i < 0 or j < 0:
                return 0
            if i == row - 1 and j == col - 1:
                return 1
            if memo[i][j] != 0:
                return memo[i][j]
            down = util(i+1, j)
            right = util(i, j + 1)
            memo[i][j] = down + right
            return memo[i][j]
        return util(0, 0)