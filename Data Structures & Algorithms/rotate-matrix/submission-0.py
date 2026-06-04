class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(row):
            for j in range(col // 2):
                left = j
                right = col - j - 1
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]

        
        
