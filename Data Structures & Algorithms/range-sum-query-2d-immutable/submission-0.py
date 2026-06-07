class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        row = len(self.matrix)
        col = len(self.matrix[0])

        # calc pref
        for j in range(1, col):
            self.matrix[0][j] += self.matrix[0][j-1]
        for i in range(1, row):
            self.matrix[i][0] += self.matrix[i-1][0]

        for i in range(1, row):
            for j in range(1, col):
                self.matrix[i][j] += matrix[i-1][j] + matrix[i][j - 1] - matrix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        d = u = l = 0
        diagR = row1 - 1
        diagC = col1 - 1
        

        upR = row1 - 1
        upC = col2

        leftR = row2
        leftC = col1 - 1

        if diagR < 0 or diagC < 0:
            d = 0
        else:
            d = self.matrix[diagR][diagC]
        
        if upR < 0:
            u = 0
        else:
            u = self.matrix[upR][upC]

        if leftC < 0:
            l = 0
        else:
            l = self.matrix[leftR][leftC]



        val = self.matrix[row2][col2]
        # print(self.matrix)
        # print(val, u, l, d)

        return val - (u + l) + d

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)