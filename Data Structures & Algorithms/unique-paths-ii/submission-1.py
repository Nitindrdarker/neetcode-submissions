class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0

        memo = [[0 for i in range(col)]for j in range(row)]
        memo[-1][-1] = 1
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if i == row - 1 and j == col - 1:
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                right = down = 0
                if j + 1 < col:
                    right = memo[i][j+1]
                if i + 1 < row:
                    down = memo[i+1][j]
                memo[i][j] = right + down
        return memo[0][0]
