class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        def util(i, j):
            if i >= row or j >= col or i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            if i == row - 1 and j == col - 1:
                return 1
            if (i, j) in memo:
                return memo[(i,j)]

            right = util(i, j + 1)
            left = util(i + 1, j)
            memo[(i, j)] = right + left
            return memo[(i, j)]
        return util(0, 0)

      
