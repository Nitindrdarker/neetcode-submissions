class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colVisited = set()
        posDiagVisited = set()
        negDiagVisited = set()
        row = col = n
        curr = [['.' for i in range(col)] for j in range(row)]
        res = []
        def util(i):
            if i >= row:
                temp = []
                for c in curr:
                    temp.append(''.join(c))
                res.append(temp)
                return
            
            for j in range(col):
                if j in colVisited:
                    continue
                posDiag = i - j
                negDiag = i + j
                if posDiag in posDiagVisited:
                    continue
                if negDiag in negDiagVisited:
                    continue
                colVisited.add(j)
                posDiagVisited.add(posDiag)
                negDiagVisited.add(negDiag)
                curr[i][j] = 'Q'
                util(i+1)
                curr[i][j] = '.'
                colVisited.remove(j)
                posDiagVisited.remove(posDiag)
                negDiagVisited.remove(negDiag)
        util(0)
        return res

                
            

            