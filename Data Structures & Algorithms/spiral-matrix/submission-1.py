class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = 0
        rs, cs = 0, 0
        re, ce = row - 1, col - 1
        res = []

        while i >= rs and i <= re and j >= cs and j <= ce:
            
            #right
            while rs <= re and cs <= ce and j <= ce:
                res.append(matrix[i][j])
                j += 1
            rs += 1
            j -= 1
            i += 1

            

            
            #down
            while rs <= re and cs <= ce and i <= re:
                res.append(matrix[i][j])
                i += 1
            ce -= 1
            i -= 1
            j -= 1


            # right
            while rs <= re and cs <= ce and j >= cs:
                res.append(matrix[i][j])
                j -= 1
            re -= 1
            j += 1
            i -= 1

            #up
            while rs <= re and cs <= ce and  i >= rs:
                res.append(matrix[i][j])
                i -= 1
            i += 1
            cs += 1
            j += 1

        return res

            



